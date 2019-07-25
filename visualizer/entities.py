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


class ColumnHeader:
    def __init__(self, id: str, label: str, type: str):
        self.id = id
        self.label = label
        self.type = type


class ChartEntity:
    def __init__(self, columns: List[ColumnHeader], rows: List[ChartRow]):
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

class ValueObject:
    def __init__(self, value, label):
        self.value = value
        self.label = label

    def __repr__(self):
        return "Object(%s, %s)" % (self.value, self.label)

    def __eq__(self, other):
        if isinstance(other, ValueObject):
            return ((self.value == other.value) and (self.label == other.label))
        else:
            return False

    def __ne__(self, other):
        return (not self.__eq__(other))

    def __hash__(self):
        return hash(self.__repr__())