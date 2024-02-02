import csv
import json

def parse_txt_to_json(input_file):
    json_data = []

    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter='|')

        for row in reader:
            json_data.append(row)

    return json_data

input_file = 'data.txt'
output_json_array = parse_txt_to_json(input_file)

with open('output.json', 'w', encoding='utf-8') as json_file:
    json.dump(output_json_array, json_file, ensure_ascii=False, indent=2)
