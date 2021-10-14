'''
    Simple Schemas for Olympic dataset taken from https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results

    Author: Thien K. M. Bui 10-11-21

    Credit: Dani Bottiger for giving useful suggestions for per_olympic_athlete and table_earned tables 

'''


CREATE TABLE athletes (
    id SERIAL,
    full_name text,
    first_name text,
    last_name text,
    sex text
);

CREATE TABLE nocs_teams (
    id SERIAL,
    noc text UNIQUE,
    team text,
    region text,
    notes text
);

CREATE TABLE olympics (
    id SERIAL,
    year integer UNIQUE,
    season text,
    game text,
    city text
);

CREATE TABLE olympics_athletes(
    athlete_id integer,
    olympic_id integer,
    noc_id integer,
    height integer,
    weight integer,
    age integer
);

CREATE TABLE olympics_medals(
    athlete_id integer,
    olympic_id integer,
    sport text,
    event text,
    medal text
);
