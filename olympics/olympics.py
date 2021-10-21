'''
    Simple CLI for printing Olympic data taken from https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results .

    Data is queued from a postgresql database version 12.8 (Ubuntu 12.8-0ubuntu0.20.04.1)

    config.py needs to include db's username, password, and database name

    Author: Thien K. M. Bui, 10-19-2021
'''


import argparse
import psycopg2

# import provided credentials
from config import password
from config import database
from config import username


def parsed_arguments():
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('--noc', '-n')
    parser.add_argument('--medals', '-m', action='store_true')
    parser.add_argument('--athletes', '-a')

    parser.add_argument('-h', '--help', action='store_true')

    return parser.parse_args()


def open_help():
    file = open('usage.txt', 'r')
    content = file.read()
    print(content)
    file.close()


def connect_to_db():
    pass


if __name__ == "__main__":
    arguments = parsed_arguments()

    # no arguments were provided
    if not arguments.noc and not arguments.medals and not arguments.help and not arguments.athletes:
        user_input = input(
            "Please provide a valid argument, type \'help\' to see usage.txt: ")
        if(user_input == "help"):
            open_help()
            exit()
        else:
            exit()

    if arguments.help:
        open_help()
        exit()

    # connect to databse
    try:
        connection = psycopg2.connect(
            database=database, user=username, password=password)
    except Exception as e:
        print(e, "unable to connect to databse --KB")
        exit()

    # cursor to be used for queries
    cursor = connection.cursor()

    if arguments.noc:
        formatted_search_string = str(arguments.noc).upper()

        noc_query = '''
            SELECT DISTINCT athletes.last_name, athletes.first_name, athletes.full_name, nocs_teams.noc
            FROM athletes, nocs_teams, olympics_athletes
            WHERE athletes.id = olympics_athletes.athlete_id
            AND nocs_teams.id = olympics_athletes.noc_id
            AND nocs_teams.noc LIKE %s
            ORDER by athletes.last_name;
            '''
        try:
            cursor.execute(noc_query, (formatted_search_string,))
        except Exception as e:
            print(e, "noc_query --KB")
            exit()

        # formatting so output looks nice
        print('===================',
              'athletes from NOC %s' % (formatted_search_string), '===================\n')
        print("{:<15} {:<20} {:<45} {:<10}".format(
            "Last name", "First name", "Full name", "NOC"))
        for row in cursor:
            print("{:<15} {:<20} {:<45} {:<10}".format(
                row[0], row[1], row[2], row[3]))
        print('================================================================================\n\n')

    if arguments.medals:
        medals_query = '''
            SELECT nocs_teams.noc, nocs_teams.team, COUNT(olympics_medals.medal)
            FROM nocs_teams, olympics_medals, olympics_athletes
            WHERE (olympics_medals.medal LIKE 'Gold' OR olympics_medals.medal IS NULL)
            AND olympics_medals.athlete_id = olympics_athletes.athlete_id
            AND olympics_athletes.noc_id = nocs_teams.id
            GROUP BY nocs_teams.noc, nocs_teams.team
            ORDER BY COUNT(olympics_medals.medal) DESC;
        '''

        try:
            cursor.execute(medals_query)
        except Exception as e:
            print(e, "medals_query --KB")
            exit()

        # formatting so output looks nice
        print('===================',
              'Gold medals earned by each NOC in database', '===================\n')
        print("{:<15} {:<30} {:<45}".format(
            "NOC", "Team Name", "Gold medals earned", "NOC"))
        for row in cursor:
            print("{:<15} {:<30} {:<45}".format(
                row[0], row[1], row[2]))
        print('================================================================================\n\n')

    if arguments.athletes:

        # so that 'louGanis' will return results for athlete "Louganis"
        formatted_search_string = arguments.athletes.lower()

        athletes_query = '''
            SELECT athletes.last_name, athletes.first_name, athletes.full_name, COUNT(olympics_medals.medal)
            FROM olympics_medals, athletes
            WHERE POSITION(%s IN LOWER(athletes.full_name)) > 0
            AND athletes.id = olympics_medals.athlete_id
            AND (olympics_medals.medal LIKE 'Gold' OR olympics_medals.medal IS NULL)
            GROUP BY athletes.last_name, athletes.first_name, athletes.full_name
            ORDER BY COUNT(olympics_medals.medal) DESC;
        '''

        try:
            cursor.execute(athletes_query, (formatted_search_string,))
        except Exception as e:
            print(e, "athletes_query --KB")
            exit()

        # formatting so output looks nice
        print('===================',
              'Gold medals earned by athletes whose names contains %s' % (formatted_search_string), '===================\n')
        print("{:<15} {:<30} {:<45} {:10}".format(
            "First name", "Last name", "Full name", "Gold medals earned"))
        for row in cursor:
            print("{:<15} {:<30} {:<45} {:10}".format(
                row[0], row[1], row[2], row[3]))
        print('================================================================================\n\n')

    # because we need to close it
    connection.close()
