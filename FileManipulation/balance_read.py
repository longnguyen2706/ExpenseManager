import pandas as pd

from FileManipulation.pdf_read import pdf_to_excel
from FileManipulation.read_util import filter_by_cols, get_file_in_resource

RESOURCE_FOLDER = "../resources"
EXCEL_FILE = "../resources/DBS_Jan19.xlsx"

COLUMN_TYPES= {"Balance": float,"Date": str, "Deposit": float, "Description": str, "Withdrawal": str}
COLUMN_NAMES = ["Balance","Date", "Deposit", "Description", "Withdrawal"]

def balance_read(file_path):
    pdf_to_excel(file_path)


def main():
    balance_read("")

if __name__ == "__main__":
    main()