import csv
from typing import AsyncGenerator
with open('Python Developer Test Dataset.csv', mode='r') as db:
    csv_reader = csv.DictReader(db)
    column_list = db.readline().split(',')  # read only the first line
    print(*([x for x in enumerate(column_list)]), sep='\n')

    def get_option():
        return f"{display_option(int(input('please inform an option number: ')))}"

    def display_option(option):
        return [x[0] for x in enumerate(column_list) if option == x[0]][0]

print(get_option())


with open('Python Developer Test Dataset.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        column_names = {", ".join(row)}

        print(row['Property Name'])