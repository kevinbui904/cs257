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
    parser.add_argument('--medals', '-m')

    parser.add_argument('-h', '--help', action='store_true')

    return parser.parse_args()


def print_help():
    file = open('usage.txt', 'r')
    content = file.read()
    print(content)
    file.close()


def connect_to_db():
    pass


if __name__ == "__main__":
    arguments = parsed_arguments()

    # no arguments were provided
    if(not arguments.noc and not arguments.medals and not arguments.help):
        user_input = input(
            "Please provide a valid argument, type \'help\' to see usage.txt: ")
        if(user_input == "help"):
            print_help()
            exit()
        else:
            exit()

    if(arguments.help):
        print_help()
        exit()

    # connect to databse
    try:
        connection = psycopg2.connect(
            database=database, user=username, password=password)
    except Exception as e:
        print(e, "unable to connect to databse --KB")
        exit()

    try:
        cursor = connection.cursor()
    except Exception as e:
        print(e, "unable to instantiate cursor --KB")
        exit()

    if(arguments.noc):
        sanitized_search_string = str(arguments.noc).upper()

        noc_query = '''
            SELECT DISTINCT athletes.last_name, athletes.first_name, athletes.full_name, nocs_teams.noc
            FROM athletes, nocs_teams, olympics_athletes
            WHERE athletes.id = olympics_athletes.athlete_id
            AND nocs_teams.id = olympics_athletes.noc_id
            AND nocs_teams.noc LIKE %s
            ORDER by athletes.last_name;
            '''
        cursor.execute(noc_query, (sanitized_search_string,))
        print('===================',
              'athletes from NOC %s' % (sanitized_search_string), '===================\n\n')
        print("{:<15} {:<20} {:<45} {:<10}".format(
            "last_name", "first_name", "full_name", "NOC"))
        for row in cursor:
            print("{:<15} {:<20} {:<45} {:<10}".format(
                row[0], row[1], row[2], row[3]))

    elif (arguments.medals):
        pass
