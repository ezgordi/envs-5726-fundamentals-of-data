from pathlib import Path
import csv

csv_path = Path(r'C:\Users\egordi\Downloads\Haiti_Earthquake_Damage_Assessment.csv')
haiti_earthquake_table = []

with open(csv_path, 'r', encoding = 'utf-8') as csv_file:
    reader = csv.reader(csv_file)

    headers = next(reader)

    for row in reader:
        haiti_earthquake_table.append(row)

print('these are the headers:')
print(headers)

print('these are the rows:')
print(haiti_earthquake_table)
for row in haiti_earthquake_table:
    print(row)


number_of_rows = len(haiti_earthquake_table)
print(f' There are {number_of_rows} rows in {csv_path.stem}')

damaged_building_column = []
for row in haiti_earthquake_table:
    damaged_building_column.append(row[headers.index('Damaged Buildings')])
print(damaged_building_column)
