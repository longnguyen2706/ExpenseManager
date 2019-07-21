from typing import List

from datetime import date

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
