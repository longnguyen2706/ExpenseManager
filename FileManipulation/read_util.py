import os
import pandas as pd
from typing import List

RESOURCE_FOLDER = "../resources"

def get_resource():
    curr_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_path, RESOURCE_FOLDER)

def get_file_in_resource(file_name):
    curr_path = os.path.abspath(os.path.dirname(__file__))
    return os.path.join(curr_path, file_name)


def find_header_idx(df:pd.DataFrame, columns:List[str]) -> int:
    for idx, data in df.iterrows():
        items = set(data.tolist())
        if(set(columns).issubset(items)):
            return idx
    return -1

def print_by_col(df: pd.DataFrame):
    for label, content in df.iteritems():
        print('label:', label)
        print('content:', content, sep='\n')

def print_by_row(df: pd.DataFrame):
    for idx, data in df.iterrows():
        print(data.tolist())

def filter_by_cols(df, columns):
    # drop col that has all NAN val
    df = df.dropna(axis=1, how='all')

    # set df column to row that contain columns
    hd_idx = find_header_idx(df, columns)

    # header not found!
    if (hd_idx == -1):
        return pd.DataFrame()
    else:
        df.columns = df.iloc[hd_idx]
        # take columns that is in columns list only
        return df.loc[hd_idx+1:, df.columns.isin(columns)]
