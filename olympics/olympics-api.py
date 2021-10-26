'''
    olympics-api.py 
    Kevin Bui, 24 October 2021
    Updated 24 October 2021

    HTML-based API implementation of olympics.sql database using Flask
'''

import sys
import argparse
import json
import flask
import psycopg2

# import provided credentials
import config

app = flask.Flask(__name__)

# API routes


@app.route('/')
def hello():
    return "Hello world, this is an implementation of Olympic Flask API for CS257 Fall 2021"


'''
RESPONSE: a JSON list of dictionaries, each of which represents one
Olympic games, sorted by year. Each dictionary in this list will have
the following fields.

   id -- (INTEGER) a unique identifier for the games in question
   year -- (INTEGER) the 4-digit year in which the games were held (e.g. 1992)
   season -- (TEXT) the season of the games (either "Summer" or "Winter")
   city -- (TEXT) the host city (e.g. "Barcelona")
'''


@app.route('/games')
def get_games():
    # connect to databse
    try:
        connection = psycopg2.connect(
            database=config.database, user=config.username, password=config.password)
    except Exception as e:
        print(e, "unable to connect to databse --KB")
        exit()

    games_list = []

    query = '''
        SELECT olympics.id, olympics.year, olympics.season, olympics.city
        FROM olympics
        ORDER BY olympics.year
    '''

    cursor = connection.cursor()

    try:
        cursor.execute(query)
    except Exception as e:
        print(e, "games route database error --kb")

    for row in cursor:
        id = row[0]
        year = row[1]
        season = row[2]
        city = row[3]

        game = {
            "id": id,
            "year": year,
            "season": season,
            "city": city
        }
        games_list.append(game)

    # because we need to close connection EVERYTIME
    connection.close()

    return json.dumps(games_list)


'''
RESPONSE: a JSON list of dictionaries, each of which represents one
National Olympic Committee, alphabetized by NOC abbreviation. Each dictionary
in this list will have the following fields.

   abbreviation -- (TEXT) the NOC's abbreviation (e.g. "USA", "MEX", "CAN", etc.)
   name -- (TEXT) the NOC's full name (see the noc_regions.csv file)
'''


@app.route('/nocs')
def get_nocs():
    # connect to databse
    try:
        connection = psycopg2.connect(
            database=config.database, user=config.username, password=config.password)
    except Exception as e:
        print(e, "unable to connect to databse --KB")
        exit()

    noc_list = []

    query = '''
        SELECT nocs_teams.noc, nocs_teams.team
        FROM nocs_teams
        ORDER BY nocs_teams.noc
    '''

    cursor = connection.cursor()

    try:
        cursor.execute(query)
    except Exception as e:
        print(e, "noc route database error --kb")

    for row in cursor:
        abbr = row[0]
        team = row[1]

        noc = {
            "noc": abbr,
            "name": team,
        }
        noc_list.append(noc)

    # because we need to close connection EVERYTIME
    connection.close()

    return json.dumps(noc_list)


'''
RESPONSE: a JSON list of dictionaries, each representing one athlete
who earned a medal in the specified games. Each dictionary will have the
following fields.
   athlete_id -- (INTEGER) a unique identifier for the athlete
   athlete_name -- (TEXT) the athlete's full name
   athlete_sex -- (TEXT) the athlete's sex as specified in the database ("F" or "M")
   sport -- (TEXT) the name of the sport in which the medal was earned
   event -- (TEXT) the name of the event in which the medal was earned
   medal -- (TEXT) the type of medal ("gold", "silver", or "bronze")
If the GET parameter noc=noc_abbreviation is present, this endpoint will return
only those medalists who were on the specified NOC's team during the specified
games.
'''


@app.route('/medalists/games/<games_id>')
def get_medalists(games_id):

    athletes_list = []

    noc = flask.request.args.get('noc')

    if noc is not None:
        query = '''
            SELECT DISTINCT athletes.id, athletes.full_name, athletes.sex, olympics_medals.sport, olympics_medals.event, olympics_medals.medal
            FROM athletes, olympics_medals, olympics_athletes, nocs_teams
            WHERE olympics_medals.olympic_id = %(games_id)s
            AND olympics_medals.medal IS NOT NULL
            AND olympics_medals.athlete_id = olympics_athletes.athlete_id
            AND olympics_medals.athlete_id = athletes.id
            AND olympics_athletes.noc_id = nocs_teams.id
            AND nocs_teams.noc = %(noc)s
            ORDER BY athletes.id
        '''
    else:
        query = '''
            SELECT athletes.id, athletes.full_name, athletes.sex, olympics_medals.sport, olympics_medals.event, olympics_medals.medal
            FROM athletes, olympics_medals
            WHERE olympics_medals.olympic_id = %(games_id)s
            AND olympics_medals.medal IS NOT NULL
            AND olympics_medals.athlete_id = athletes.id
            ORDER BY athletes.id
        '''
    # connect to database
    try:
        connection = psycopg2.connect(
            database=config.database, user=config.username, password=config.password)
    except Exception as e:
        print(e, "unable to connect to databse --KB")
        exit()

    cursor = connection.cursor()
    try:
        cursor.execute(query, {'games_id': games_id, 'noc': noc})
    except Exception as e:
        print(e, " medalists route db error --kb")

    for row in cursor:
        id = row[0]
        name = row[1]
        sex = row[2]
        sport = row[3]
        event = row[4]
        medal = row[5]

        athlete = {
            "id": id,
            "name": name,
            "sex": sex,
            "sport": sport,
            "event": event,
            "medal": medal
        }

        athletes_list.append(athlete)

    # because we need to close connection EVERYTIME
    connection.close()
    return json.dumps(athletes_list)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'host', help='the host on which this application is running')
    parser.add_argument(
        'port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()

    app.run(host=arguments.host, port=arguments.port, debug=True)
