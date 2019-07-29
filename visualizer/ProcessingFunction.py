from visualizer.entities import ValueObject
import decimal
from datetime import date, time
from typing import List
from .models import *

class ProcessingFunction:
    def __init__(self):
        pass

    # x_process
    def date_to_year(self, d: date):
        return ValueObject(d.year, str(d.year))

    def date_to_month(self, d: date):
        return ValueObject(d.month, d.strftime('%B'))

    def date_to_month_year(self, d: date):
        return ValueObject (d.year*1000+ d.month, d.strftime('%B') + ", " + str(d.year))

    def do_nothing(self, x):
        return ValueObject(x, x)

    # y_process
    def sum_by_group(self, field_name: str, records: List[List[SuperStore]]):
        sums = [sum(map(lambda x: getattr(x, field_name), l)) for l in records]
        return sums

    def process_nothing(self,  field_name: str, records: List[List[SuperStore]]):
        return []

    def count_frequency(self, field_name: str, records: List[List[SuperStore]]):
        result = []
        for cat_records in records:
            values = sorted(set(map(lambda x: getattr(x, field_name), cat_records)))
            newlist = [[y for y in cat_records if getattr(y, field_name) == x] for x in values]
            result.append(len(newlist))
        print (result)
        return result

    def count (self, field_name: str, records: List[List[SuperStore]]):
        return [len(a) for a in records]

    def get_value_obj_key(self, v: ValueObject):
        return v.value