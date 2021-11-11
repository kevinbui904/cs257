'''
    disney-api.py
    Authors: Kevin Bui, Robbie Young, November 11 2021
    * add desc of doc
    For use in the final project in Carleton College's CS 257 Software Design Class, Fall 2021
'''

# * seems like all LIKE statements in queries only return exact matches, could be different when running through a web app instead of natively python

import flask
import json
import psycopg2
import argparse
import config
from config import database as config_database
from config import user as config_user
from config import password as config_password

app = flask.Flask(__name__)

def connect(connect_database, connect_user, connect_password):
    try:
        connection = psycopg2.connect(database=connect_database, user=connect_user, password=connect_password)
        return connection
    except Exception as e:
        print(e)
        exit()

def create_list(cursor):
    content_list = []

    for this_content in cursor:
        this_dict = {}
        this_dict['type'] = cursor[0]
        this_dict['title'] = cursor[1]
        this_dict['directors'] = cursor[2]
        this_dict['cast'] = cursor[3]
        this_dict['date_added'] = cursor[4]
        this_dict['release_year'] = cursor[5]
        this_dict['rating'] = cursor[6]
        this_dict['duration'] = cursor[7]
        this_dict['listed_in'] = cursor[8]
        this_dict['description'] = cursor[9]
        content_list.append(this_dict)
    
    return content_list

@app.route('/recommended')
def genre():
    connection = connect(config_database, config_user, config_password)
    genre = flask.request.args.get('genre')
    query = '''SELECT type, title, director, actors, date_added, release_year, rating, duration, genres, description
                FROM countries, date_added, genres, rating, super_table, type
                WHERE super_table.countries_id = countries.id
                AND super_table.date_added_id = date_added.id
                AND super_table.genres_id = genres.id
                AND super_table.rating_id = rating.id
                AND super_table.type_id = type.id'''
    
    try:
        cursor = connection.cursor()
        if genre is not None:
            query =+ '''AND genres.genres LIKE %s
                        ORDER BY RANDOM()
                        LIMIT 1'''
            cursor.execute(query, (genre, ))
        else:
            query =+ '''ORDER BY RANDOM()
                        LIMIT 1'''
            cursor.execute(query)
    except Exception as e:
        connection.close()
        print(e)
        exit()

    content_list = create_list(cursor)
    connection.close()
    return json.dumps(content_list)

# * for genre, to keep the scope of this project simple, the only genre they could select from is "action", "comedy", "horror", "documentary", "sci-fi"

@app.route('/directors/<directors_name>')
def director():
    connection = connect(config_database, config_user, config_password)
    sort_by = flask.request.args.get('sort_by')
    query = '''SELECT type, title, director, actors, date_added, release_year, rating, duration, genres, description
                FROM countries, date_added, genres, rating, super_table, type
                WHERE super_table.countries_id = countries.id
                AND super_table.date_added_id = date_added.id
                AND super_table.genres_id = genres.id
                AND super_table.rating_id = rating.id
                AND super_table.type_id = type.id
                AND super_table.director LIKE %s'''
    
    try:
        cursor = connection.cursor()
        if sort_by is not None:
            query =+ '''SORT BY %s'''
            cursor.execute(query, (sort_by, ))
        else:
            query =+ '''SORT BY title'''
            cursor.execute(query)
    except Exception as e:
        connection.close()
        print(e)
        exit()

    content_list = create_list(cursor)
    connection.close()
    return json.dumps(content_list)
# * let's restrict searches ONLY to 1 author at a time

@app.route('/titles/<titles_string>')
def titles():
    connection = connect(config_database, config_user, config_password)
    sort_by = flask.request.args.get('sort_by')
    query = '''SELECT type, title, director, actors, date_added, release_year, rating, duration, genres, description
                FROM countries, date_added, genres, rating, super_table, type
                WHERE super_table.countries_id = countries.id
                AND super_table.date_added_id = date_added.id
                AND super_table.genres_id = genres.id
                AND super_table.rating_id = rating.id
                AND super_table.type_id = type.id
                AND super_table.title LIKE %s'''
    
    try:
        cursor = connection.cursor()
        if sort_by is not None:
            query =+ '''SORT BY %s'''
            cursor.execute(query, (sort_by, ))
        else:
            query =+ '''SORT BY title'''
            cursor.execute(query)
    except Exception as e:
        connection.close()
        print(e)
        exit()

    content_list = create_list(cursor)
    connection.close()
    return json.dumps(content_list)

@app.route('/cast/<cast_name>')
def cast():
    connection = connect(config_database, config_user, config_password)
    sort_by = flask.request.args.get('sort_by')
    query = '''SELECT type, title, director, actors, date_added, release_year, rating, duration, genres, description
                FROM countries, date_added, genres, rating, super_table, type
                WHERE super_table.countries_id = countries.id
                AND super_table.date_added_id = date_added.id
                AND super_table.genres_id = genres.id
                AND super_table.rating_id = rating.id
                AND super_table.type_id = type.id
                AND super_table.actors LIKE %s'''
    
    try:
        cursor = connection.cursor()
        if sort_by is not None:
            query =+ '''SORT BY %s'''
            cursor.execute(query, (sort_by, ))
        else:
            query =+ '''SORT BY title'''
            cursor.execute(query)
    except Exception as e:
        connection.close()
        print(e)
        exit()

    content_list = create_list(cursor)
    connection.close()
    return json.dumps(content_list)
# * let's restrict searches ONLY to 1 cast at a time

def main():
    parser = argparse.ArgumentParser('Flask application for the disney web application')
    parser.add_argument('host', help='the host on which this application is running')
    parser.add_argument('port', type=int, help='the port on which this application is listening')
    arguments = parser.parse_args()
    app.run(host=arguments.host, port=arguments.port, debug=True)

if __name__ == '__main__':
    main()