'''
    Parse athlete_events.csv and noc_region.csv to be loaded into custom PSQL schemas
    src: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results
    at 21:00 10-11-21

    "ID","Name","Sex","Age","Height","Weight","Team","NOC","Games","Year","Season","City","Sport","Event","Medal"
    NOC,region,notes
    Author: Thien K. M. Bui, 10-11-2021
'''

import csv

if __name__ == "__main__":
    new_athletes_file = open('./athletes.csv', 'w')
    athletes_writer = csv.writer(new_athletes_file)

    new_noc_team_file = open('./nocs_teams.csv', 'w')
    noc_team_writer = csv.writer(new_noc_team_file)

    # used for checking uniqueness
    unique_athlete_dict = {}
    unique_noc_dict = {}
    # NOC used to match

    with open('athlete_events.csv') as athlete_events_file, open('noc_regions.csv') as noc_region_file:

        noc_file_reader = csv.reader(noc_region_file)
        athlete_file_reader = csv.reader(athlete_events_file)
        # create athletes.csv

        athletes_count = 0
        skip_athlete_events = True
        for row in athlete_file_reader:
            # skip the first row of both readers, redundant column names
            if(skip_athlete_events):
                skip_athlete_events = False
            else:
                athlete_id = row[0]
                # only write to athletes.csv if athlete is unique based on data set provided id
                if(not unique_athlete_dict.get(athlete_id, False)):
                    athletes_count += 1
                    unique_athlete_dict[athlete_id] = True

                    athlete_name = row[1]
                    name_destructured = athlete_name.split(' ')
                    last_name = name_destructured[-1]
                    first_name = name_destructured[0]

                    athlete_sex = row[2]
                    athletes_writer.writerow(
                        [athlete_id, athlete_name, first_name, last_name, athlete_sex])

                # noc are inconsistent in athlete_event.csv and noc_regions.csv (Singapore is SIN in noc_regions and SGP in athlete_events), we will take the version shown in athlete_event since it'll be used to link athletes with their team/country later
                noc = row[7].replace("\"", '')
                team = row[6]
                if(not unique_noc_dict.get(noc, False)):
                    unique_noc_dict[noc] = team

        # write out to noc_regions.csv
        skip_noc = True
        noc_id = 0
        for row in noc_file_reader:
            if(skip_noc):
                skip_noc = False
            else:
                noc = row[0]
                region = row[1]
                notes = row[2]

                # if the noc doesn't exist here after parsing athlete_events, there's inconsistencies so we need to parse the value of "team" from athlete_events and compare it with "region" from athlete_events.csv
                if(not unique_noc_dict.get(noc, False)):
                    written = False
                    for key in unique_noc_dict.keys():
                        if(unique_noc_dict.get(noc, False) and region in unique_noc_dict[noc]):
                            written = True
                            # prioritize the NOC spelling in athlete_events
                            noc_team_writer.writerow(
                                [noc_id, key, unique_noc_dict[key], region, notes])

                    # we only want to write to csv ONCE per new noc we haven't encountered
                    if(not written):
                        print([noc_id, noc, None, region, notes], "check this")
                        noc_team_writer.writerow(
                            [noc_id, noc, None, region, notes])

                else:
                    noc_team_writer.writerow(
                        [noc_id, noc, unique_noc_dict[noc], region, notes])

                noc_id += 1

        print(noc_id, " # of noc")
        print(athletes_count, " # of athletes")
