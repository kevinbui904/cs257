'''
    Simple queries for Olympic schemas defined in olympics_schema.sql

    Author: Thien K. M. Bui 10-14-21

'''

-- all NOC listed in alphabetical order by NOC abbreviations
SELECT * FROM nocs_teams
ORDER by nocs_teams.noc;

-- names of all athletes from Kenya sorted alphabetically by last name
SELECT DISTINCT athletes.last_name, athletes.first_name, athletes.full_name, nocs_teams.noc
FROM athletes, nocs_teams, olympics_athletes
WHERE athletes.id = olympics_athletes.athlete_id
AND nocs_teams.id = olympics_athletes.noc_id
AND nocs_teams.noc LIKE 'KEN'
ORDER by athletes.last_name;


-- all medals won by Greg Louganis, sorted by olympic year
SELECT DISTINCT olympics.year, olympics_medals.medal, olympics_medals.sport, nocs_teams.team, olympics_medals.event, nocs_teams.team, athletes.full_name
FROM olympics_medals, olympics, athletes, nocs_teams, olympics_athletes
WHERE athletes.full_name LIKE '%Greg%' 
AND athletes.full_name LIKE '%Louganis%'
-- comment for future reference, NULL is treated as not equal/equal to ANYTHING in PSQL. Could've realistically replaced 'NULL' with <ANYTHING> and this query would've worked. The clause below reads "give me back everything that DOES NOT look like the parameter, dataset only have Gold, Silver, Bronze, and NULL"
AND olympics_medals.medal NOT LIKE 'NULL'
AND athletes.id = olympics_medals.athlete_id
AND olympics.id = olympics_medals.olympic_id
AND athletes.id = olympics_athletes.athlete_id
AND nocs_teams.id = olympics_athletes.noc_id
ORDER by olympics.year;

-- noc and all gold medals they've won, sorted in decreasing order by number of gold medals won
SELECT nocs_teams.noc, nocs_teams.team, COUNT(olympics_medals.medal) as "Gold medals earned"
FROM nocs_teams, olympics_medals, olympics_athletes
WHERE olympics_medals.medal LIKE 'Gold'
AND olympics_medals.athlete_id = olympics_athletes.athlete_id
AND olympics_athletes.noc_id = nocs_teams.id
GROUP BY nocs_teams.noc, nocs_teams.team
ORDER BY COUNT(olympics_medals.medal) DESC;







