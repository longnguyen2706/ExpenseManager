import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os

import xlrd
from openpyxl.workbook import Workbook
from openpyxl.reader.excel import load_workbook, InvalidFileException

RESOURCE_FOLDER = "../resources"
EXCEL_FILE = "../resources/DBS_Jan19.xlsx"
# PDF_FILE = "../resources/DBS_Mar19.pdf"
PDF_FILE = "../resources/FRANK ACCOUNT-0001-Apr-19.pdf"
COLUMN_TYPES= {"Balance": float,"Date": str, "Deposit": float, "Description": str, "Withdrawal": str}
COLUMN_NAMES = ["Balance","Date", "Deposit", "Description", "Withdrawal"]

def read_excel(file_path):

    # open_xls_as_xlsx(file_path)
    df = pd.read_excel(file_path, sheet_name=1, header =7, usecols=COLUMN_NAMES, keep_default_na=False)
    [print(i) for i in df.items()]

def read_pdf(file_path):
    import tabula

    columns =['Date', 'Date', 'Description', 'Cheque', 'Withdrawal', 'Deposit', 'Balance']
    # Read pdf into DataFrame

    df_list = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

    # df = df.dropna(axis=1, how='all')
    for df in df_list:
        df = df.dropna(axis=1, how='all')
        df.columns = df.iloc[1]
        print(df.columns)
        df = df.loc[:, df.columns.isin(columns)]
        print(df.columns)
        # for label, content in df.iteritems():
        #     print('label:', label)
        #     print('content:', content, sep='\n')



    # convert PDF into CSV
    # csv =  tabula.convert_into(file_path, "output.", output_format="xlsx", pages='all')

def get_resource():
    curr_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_path, RESOURCE_FOLDER)

def get_file_in_resource(file_name):
    curr_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_path, file_name)


def main():
    # excel_path = get_file_in_resource(EXCEL_FILE)
    # read_excel(excel_path)

    pdf_path = get_file_in_resource(PDF_FILE)
    read_pdf(pdf_path)

if __name__ == "__main__":
    main()