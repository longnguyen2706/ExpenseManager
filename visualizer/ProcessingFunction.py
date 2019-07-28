from visualizer.entities import ValueObject
import decimal
from datetime import date, time
from typing import List
from .models import *

class ProcessingFunction:
    def __init__(self):
        pass

    def date_to_year(self, d: date):
        return ValueObject(d.year, str(d.year))

    def date_to_month(self, d: date):
        return ValueObject(d.month, d.strftime('%B'))

    def do_nothing(self, x):
        return ValueObject(x, x)

    def sum_by_group(self, field_name: str, records: List[List[SuperStore]]):
        sums = [sum(map(lambda x: getattr(x, field_name), l)) for l in records]
        return sums

