import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import os

import xlrd
from openpyxl.workbook import Workbook
from openpyxl.reader.excel import load_workbook, InvalidFileException

RESOURCE_FOLDER = "../resources"
EXCEL_FILE = "../resources/DBS_Jan19.xlsx"
COLUMN_TYPES= {"Balance": float,"Date": str, "Deposit": float, "Description": str, "Withdrawal": str}
COLUMN_NAMES = ["Balance","Date", "Deposit", "Description", "Withdrawal"]

def read_excel(file_path):

    # open_xls_as_xlsx(file_path)
    df = pd.read_excel(file_path, sheet_name=1, header =7, usecols=COLUMN_NAMES, keep_default_na=False)
    [print(i) for i in df.items()]

def get_resource():
    curr_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_path, RESOURCE_FOLDER)

def get_file_in_resource(file_name):
    curr_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_path, file_name)


def main():
    excel_path = get_file_in_resource(EXCEL_FILE)
    read_excel(excel_path)


if __name__ == "__main__":
    main()