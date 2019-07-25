from datetime import date, time
from typing import List

from visualizer.entities import *
from visualizer.models import *


def group_by(field_name: str, f, records: List[SuperStore]):
    values = sorted(set(map(lambda x: f(getattr(x, field_name)), records)))
    newlist = [[y for y in records if f(getattr(y, field_name)) == x] for x in values]
    return list(values), newlist

def date_to_year(d: date):
    return d.year

def date_to_month(d: date):
    return d.month

def get_all_values(f, l:List):
    values = sorted(set(map(lambda x: f(x), l)))
    return values

def sum_by_group(field_name: str,  records: List[List[SuperStore]]):
    sums = [sum(map(lambda x: getattr(x, field_name), l)) for l in records]
    return sums

def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, time):
        serial = obj.isoformat()
        return serial

    return obj.__dict__

def get_table_entity(cols: List[str], rows: [List[str]]):
    p_rows = []
    p_cols = [str(c) for c in cols]
    for r in rows:
        p_rows.append(dict(zip(p_cols, r)))
    return TableEntity(p_cols, p_rows)
    
def get_chart_entity(labels: List[str], sums: [List[int]]):
    columns = [ChartColumnHeader(str(l), str(l), "string") for l in labels]
    rows = []
    for s in sums:
        row_data = [RowCell(v,'') for v  in s]
        row = ChartRow(row_data, '', '')
        rows.append(row)

    return ChartEntity(columns, rows)
