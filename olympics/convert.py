'''
    Parse athlete_events.csv and noc_region.csv to be loaded into custom PSQL schemas
    src: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results
    at 21:00 10-14-21

    Author: Thien K. M. Bui, 10-19-2021

    Updated Oct 25 2021
'''

import csv

if __name__ == "__main__":
    new_athletes_file = open('./csv-dump/athletes.csv', 'w')
    athletes_writer = csv.writer(new_athletes_file)

    new_noc_team_file = open('./csv-dump/nocs_teams.csv', 'w')
    noc_team_writer = csv.writer(new_noc_team_file)

    new_olympics_file = open('./csv-dump/olympics.csv', 'w')
    olympics_writer = csv.writer(new_olympics_file)

    new_olympics_athlete_file = open('./csv-dump/olympics_athletes.csv', 'w')
    olympics_athletes_writer = csv.writer(new_olympics_athlete_file)

    new_olympics_medals_file = open('./csv-dump/olympics_medals.csv', 'w')
    olympics_medals_writer = csv.writer(new_olympics_medals_file)

    # used for checking uniqueness
    unique_athlete = {}
    unique_noc = {}
    unique_olympic_game = {}
    # NOC used to match

    with open('athlete_events.csv') as athlete_events_file, open('noc_regions.csv') as noc_region_file:

        noc_file_reader = csv.reader(noc_region_file)
        athlete_file_reader = csv.reader(athlete_events_file)
        # create athletes.csv

        skip_athlete_events = True

        olympics_id = 0
        for row in athlete_file_reader:
            # skip the first row of both readers, redundant column names
            if(skip_athlete_events):
                skip_athlete_events = False
            else:
                athlete_id = row[0]
                # only write to athletes.csv if athlete is unique based on data set provided id
                if(not unique_athlete.get(athlete_id, False)):
                    unique_athlete[athlete_id] = True

                    athlete_name = row[1].replace(",", '')
                    name_destructured = athlete_name.split(' ')
                    last_name = name_destructured[-1]
                    first_name = name_destructured[0]

                    athlete_sex = row[2]
                    athletes_writer.writerow(
                        [athlete_id, athlete_name, first_name, last_name, athlete_sex])

                # noc are inconsistent in athlete_event.csv and noc_regions.csv (Singapore is SIN in noc_regions and SGP in athlete_events), we will take the version shown in athlete_event since it'll be used to link athletes with their team/country later
                noc = row[7].replace("\"", '')
                team = row[6]
                if(not unique_noc.get(noc, False)):
                    unique_noc[noc] = [team]

                game = row[8]

                # write out to olympics.csv
                # check year for uniqueness, there should only be 1 olympic per year
                if not unique_olympic_game.get(game, False):

                    game = row[8]
                    season = row[10]
                    city = row[11]
                    olympics_writer.writerow(
                        [olympics_id, game, season, game, city])
                    unique_olympic_game[game] = olympics_id
                    olympics_id += 1

        # write out to noc_regions.csv
        skip_noc = True
        noc_id = 0
        for row in noc_file_reader:
            if(skip_noc):
                skip_noc = False
            else:
                noc = row[0]
                region = row[1].replace(',', '')
                notes = row[2]

                # if the noc doesn't exist here after parsing athlete_events, there's inconsistencies so we need to parse the value of "team" from athlete_events and compare it with "region" from athlete_events.csv
                if(not unique_noc.get(noc, False)):
                    written = False
                    for noc_key in unique_noc.keys():
                        if(unique_noc.get(noc_key, False) and region in unique_noc[noc_key]):
                            written = True
                            # prioritize the NOC spelling in athlete_events
                            unique_noc[noc_key] = [team, noc_id]
                            noc_team_writer.writerow(
                                [noc_id, noc_key, unique_noc[noc_key][0], region, notes])

                    # we only want to write to csv ONCE per new noc we haven't encountered
                    if(not written):
                        print([noc_id, noc, None, region, notes], "check this")
                        unique_noc[noc] = [region, noc_id]

                        noc_team_writer.writerow(
                            [noc_id, noc, None, region, notes])

                else:
                    unique_noc[noc] = [unique_noc[noc][0], noc_id]
                    noc_team_writer.writerow(
                        [noc_id, noc, unique_noc[noc][0], region, notes])

                noc_id += 1
    # parse linking tables olympics_medals and olympics_athletes
    with open('athlete_events.csv') as athlete_events_file:
        skip_athlete_events = True
        athlete_file_reader = csv.reader(athlete_events_file)
        for row in athlete_file_reader:
            if(skip_athlete_events):
                skip_athlete_events = False
            else:

                athlete_id = row[0]
                olympic_id = unique_olympic_game[row[8]]
                # unique noc has array inside [team, noc_id]
                # print(unique_noc[row[7]])
                noc_id = unique_noc[row[7]][1]

                height = row[4]
                weight = row[5]
                age = row[3]

                if(height == "NA"):
                    height = 'NULL'
                if(weight == "NA"):
                    weight = 'NULL'
                if(age == "NA"):
                    age = 'NULL'

                olympics_athletes_writer.writerow(
                    [athlete_id, olympic_id, noc_id, height, weight, age])

                sport = row[12]
                event = row[13]
                medal = row[14]

                if(medal == "NA"):
                    medal = 'NULL'

                olympics_medals_writer.writerow([
                    athlete_id, olympic_id, sport, event, medal])
