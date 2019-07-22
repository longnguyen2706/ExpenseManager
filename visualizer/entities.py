from typing import List

class RowCell:
    def __init__(self, v: object, f: str):
        self.v = v
        self.f = f

class Row:
    def __init__(self, data: List[RowCell], style: str, label: str):
        self.data = data
        self.style= style
        self.label = label


class ColumnHeader:
    def __init__(self, id: str, label: str, type: str):
        self.id = id
        self.label = label
        self.type = type


class DataEntity:
    def __init__(self, columns: List[ColumnHeader], rows: List[Row]):
        self.columns = columns
        self.rows = rows
