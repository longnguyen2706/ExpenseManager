from typing import List


class RowCell:
    def __init__(self, v: object, f: str):
        self.v = v
        self.f = f

class ChartRow:
    def __init__(self, data: List[RowCell], style: str, label: str):
        self.data = data
        self.style= style
        self.label = label


class ChartColumnHeader:
    def __init__(self, id: str, label: str, type: str):
        self.id = id
        self.label = label
        self.type = type


class ChartEntity:
    def __init__(self, columns: List[ChartColumnHeader], rows: List[ChartRow]):
        self.columns = columns
        self.rows = rows

class TableEntity:
    def __init__(self, cols: List[str], rows:List):
        self.cols = cols
        self.rows = rows

class VisualizerEntity:
    def __init__(self, chart: ChartEntity, table: TableEntity):
        self.chart = chart
        self.table = table
