import os
import pandas as pd
import openpyxl

root = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'GenerateXSLXtoCSV')
path_xslx = os.path.join(root, 'xlsx_input')
path_csv = os.path.join(root, 'csv_output')

def process_single_file(xslx_path):
    filename = os.path.basename(xslx_path)
    csv_filename = filename.replace('.xlsx', '.csv')
    output_path = os.path.join(path_csv, csv_filename)

    wb = openpyxl.load_workbook(xslx_path)
    sheet_names = wb.sheetnames

    if 'LocData@Info' in sheet_names:
        wb['LocData@Info'].title = 'LocData'
        wb.save(xslx_path)

    db = pd.read_excel(xslx_path, sheet_name='LocData', header=0, skiprows=2)
    newdb = pd.DataFrame({
        "key": db["uName"],
        "original": db["English"],
        "translation": "",
        "context": db["SChinese"]
    })
    newdb.to_csv(output_path, index=False)

def main():
    xslxfiles = os.listdir(path_xslx)
    for xslxfile in xslxfiles:
        if xslxfile.endswith('.xlsx'):
            xslxpath = os.path.join(path_xslx, xslxfile)
            process_single_file(xslxpath)

if __name__ == '__main__':
    main()