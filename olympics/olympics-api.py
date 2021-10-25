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
from config import password
from config import database
from config import username

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
    pass


'''
RESPONSE: a JSON list of dictionaries, each of which represents one
National Olympic Committee, alphabetized by NOC abbreviation. Each dictionary
in this list will have the following fields.

   abbreviation -- (TEXT) the NOC's abbreviation (e.g. "USA", "MEX", "CAN", etc.)
   name -- (TEXT) the NOC's full name (see the noc_regions.csv file)
'''


@app.route('/nocs')
def get_nocs():
    pass


'''
RESPONSE: a JSON list of dictionaries, each representing one athlete
who earned a medal in the specified games. Each dictionary will have the
following fields.

If the GET parameter noc=noc_abbreviation is present, this endpoint will return
only those medalists who were on the specified NOC's team during the specified
games.
'''


@app.route('/medalists/games/<games_id>?[noc=noc_abbreviation]')
def get_medalists(games_id):
    pass

    # because we need to close it
    connection.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'host', help='the host on which this application is running')
    parser.add_argument(
        'port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()

    app.run(host=arguments.host, port=arguments.port, debug=True)

    # connect to databse
    try:
        connection = psycopg2.connect(
            database=database, user=username, password=password)
    except Exception as e:
        print(e, "unable to connect to databse --KB")
        exit()
