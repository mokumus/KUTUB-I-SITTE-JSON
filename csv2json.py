import csv
import json

# Read the CSV file
with open('verbs.csv', 'r',  encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Prepare the data for JSON
json_data = {}
current_row = None
for row in data:
    if row['id'] == '1':
      current_element = row['latin'].lower()
      current_row = {
        current_element: [
          {
            "id": int(row['id']),
            "ar": row['ar'],
            "latin": row['latin'],
            "siga": row['siga'],
            "tr": row['tr'],
          }
        ]
      }
    else:
      current_row[current_element].append(
        {
          "id": int(row['id']),
          "ar": row['ar'],
          "latin": row['latin'],
          "siga": row['siga'],
          "tr": row['tr'],
        }
      )
    json_data.update(current_row)
# Write the data to a JSON file
with open('output.json', 'w', encoding='utf-8-sig') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)
