import csv
import json

def csv_to_json(csv_filepath, json_filepath):
    with open(csv_filepath, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]
    
    with open(json_filepath, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    
    print(f'Conversie voltooid! JSON-bestand opgeslagen als {json_filepath}')

# Voorbeeldgebruik
csv_to_json('Users.csv', 'Test.json')
