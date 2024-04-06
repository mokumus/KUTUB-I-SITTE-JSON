import csv
import json

# Read the CSV file
with open('emsile-i-muttaride.csv', 'r',  encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    data = list(reader)

# Prepare the data for JSON
json_data = {}
current_row = None
for row in data:
    if row['id'] == '1':
      current_element = row['root'].lower()
      current_row = {
         # id,ar,latin,single_plural,male_female,gaib_muhattab,meaning,description,root
        current_element: [
          {
            "id": int(row['id']),
            "ar": row['ar'],
            "latin": row['latin'],
            "single_plural": row['single_plural'],
            "male_female": row['male_female'],
            "gaib_muhattab": row['gaib_muhattab'],
            "meaning": row['meaning'],
            "description": row['description'],
            "root": row['root'],
          }
        ]
      }
    else:
      current_row[current_element].append(
        {
          "id": int(row['id']),
            "ar": row['ar'],
            "latin": row['latin'],
            "single_plural": row['single_plural'],
            "male_female": row['male_female'],
            "gaib_muhattab": row['gaib_muhattab'],
            "meaning": row['meaning'],
            "description": row['description'],
            "root": row['root'],
        }
      )
    json_data.update(current_row)
# Write the data to a JSON file
with open('output-muttaride.json', 'w', encoding='utf-8-sig') as f:
    json.dump(json_data, f, ensure_ascii=False, indent=2)
