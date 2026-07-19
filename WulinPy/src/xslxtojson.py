import os
import pandas as pd
import json

root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'GenerateCSVtoXSLX')
path_xlsx = os.path.join(root, 'xlsx_output', 'output.xlsx')
out_root = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'BepInEx', 'plugins', 'Seiryu.Wulin.NET6', 'Translations')
path_json = os.path.join(out_root, 'LocData.json')

def xlsx_to_json(path_xlsx, path_json):
    db = pd.read_excel(path_xlsx, engine='openpyxl')
    json_data = []

    for index, row in db.iterrows():
        json_entry = {
            "key": row["key"],
            "Source": row["Source"],
            "Translated": "" if pd.isna(row["Translated"]) else row["Translated"]
        }
        json_data.append(json_entry)

    with open(path_json, 'w', encoding='utf-8') as json_file:
        json.dump(json_data, json_file, indent=4, ensure_ascii=False)

def main():
    xlsx_to_json(path_xlsx, path_json)

if __name__ == '__main__':
    main()
