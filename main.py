import csv
import json
import argparse

def parse_txt_to_json(input_file):
    json_data = []

    with open(input_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')

        for row in reader:
            json_data.append(row)

    return json_data

parser = argparse.ArgumentParser(description='Process input and output files.')
parser.add_argument('-i', '--input', type=str, help='Input file path', required=True)
parser.add_argument('-o', '--output', type=str, help='Output file path', required=True)

args = parser.parse_args()

input_file = args.input
output_file = args.output


output_json_array = parse_txt_to_json(input_file)

with open(output_file, 'w', encoding='utf-8') as json_file:
    json.dump(output_json_array, json_file, ensure_ascii=False, indent=2)
