'''
    Parse athlete_events.csv and noc_region.csv to be loaded into custom PSQL schemas
    src: https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results 
    at 21:00 10-11-21

    Author: Thien K. M. Bui, 10-11-2021
'''

import csv

if __name__ == "__main__":
    new_athletes_file = open('./athletes.csv', 'w')

    athletes_writer = csv.writer(new_athletes_file)

    writer.writerow("hello world")

    #parse athlete_events.csv
    with open('athlete_events.csv') as athlete_events_file:
        athlete_reader = csv.reader(athlete_events_file)
        i = 0
        for row in athlete_reader:
            i += 1
            print(', '.join(row))
            if(i==3):
                break
        
