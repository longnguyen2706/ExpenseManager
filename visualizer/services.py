from typing import List

from datetime import date, time

from visualizer.entities import ColumnHeader, RowCell, Row, DataEntity
from visualizer.models import SuperStore


def group_by(field_name: str, f, records: List[SuperStore]):
    values = sorted(set(map(lambda x: f(getattr(x, field_name)), records)))
    newlist = [[y for y in records if f(getattr(y, field_name)) == x] for x in values]
    return list(values), newlist

def date_to_year(d: date):
    return d.year

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

def get_chart_response(labels: List[str], sums: [List[int]]):
    columns = [ColumnHeader(str(l), str(l), "string") for l in labels]
    rows = []
    for s in sums:
        row_data = [RowCell(v,'') for v  in s]
        row = Row(row_data, '', '')
        rows.append(row)

    return DataEntity(columns, rows)
