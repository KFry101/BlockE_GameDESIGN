#Katie Frymire
#user searchs name and give numbers for years

import csv
with open('Names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

# Eric Idle
# John Cleese

print(row)
{'first_name': 'John', 'last_name': 'Cleese'}


Name= input("Enter a name: ")