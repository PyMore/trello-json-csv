from pprint import pprint
import json
import os                                                                          
import csv
           

with open('data.json') as file:
    data = json.load(file)

cards = data['cards']
lists = data['lists']
#print(json.dumps(data, indent=2, sort_keys=True))


with open('file.csv', mode='w') as csv_file:
    fieldnames = ['Card','Decription', 'Close']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    getList = []

    for lis in lists:
        pass


    for  card in cards:
        writer.writerow(
            {
                'Card': card['name'], 
                'Decription': card['desc'],
                'Close': card['closed']
            }
        )