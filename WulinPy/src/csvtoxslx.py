import os
import pandas as pd
import openpyxl

root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'GenerateCSVtoXSLX')
path_csv = os.path.join(root, 'csv_input')
path_xlsx = os.path.join(root, 'xlsx_output','output.xlsx')

def read_and_combine_csv(directory):
    combined_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8-sig') as f:
                lines = f.readlines()
                cleaned_data = [line.replace('\ufeff', '') for line in lines]
                cleaned_data = [line.replace('key,Source,Translated\n', '') for line in cleaned_data]
                combined_data.extend(cleaned_data)

    combined_data.insert(0, "key,Source,Translated\n")

    with open(path_xlsx, 'w', encoding='utf8') as f:
        f.writelines(combined_data)

def main():
    read_and_combine_csv(path_csv)
    df = pd.read_csv(path_xlsx)
    df.to_excel(path_xlsx, index=False, sheet_name='LocData', engine='openpyxl')

if __name__ == '__main__':
    main()