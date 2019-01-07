import csv
from downloadvideo import downloadVideo
with open('./data/names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print( row['link_m3u8'])

