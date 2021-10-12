CREATE TABLE athletes (
    id SERIAL,
    name text UNIQUE,
    sex text
);

CREATE TABLE noc_team (
    id SERIAL,
    noc text UNIQUE,
    team text,
    region text,
    notes text
);

CREATE TABLE games (
    year integer UNIQUE,
    game text,
);

CREATE TABLE game_athlete_noc(
    id SERIAL,
    year integer,
    athlete_id integer,
    noc_id integer,
);
