import decimal
from datetime import date, time
from typing import List

from visualizer.entities import *
from visualizer.models import *


def group_by(field_name: str, f, records: List[SuperStore]):
    values = sorted(set(map(lambda x: f(getattr(x, field_name)), records)), key=get_value_obj_key)
    print([v.label for v in values])
    newlist = [[y for y in records if f(getattr(y, field_name)) == x] for x in values]
    return list(values), newlist


def get_value_obj_key(v: ValueObject):
    return v.value


def get_all_values(f, l: List):
    values = sorted(set(map(lambda x: f(x), l)))
    return values


def serialize(obj):
    """JSON serializer for objects not serializable by default json code"""

    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    if isinstance(obj, time):
        serial = obj.isoformat()
        return serial
    if isinstance(obj, decimal.Decimal):
        serial = str(obj)
        return serial
    return obj.__dict__


def get_table_entity(cols: List[ValueObject], rows: [List[str]]):
    p_rows = []
    p_cols = [str(c.label) for c in cols]
    for r in rows:
        p_rows.append(dict(zip(p_cols, r)))
    return TableEntity(p_cols, p_rows)


def get_chart_entity(labels: List[str], sums: [List[int]]):
    columns = [ColumnHeader(str(l.value), l.label, "string") for l in labels]
    rows = []
    for s in sums:
        row_data = [RowCell(v, '') for v in s]
        row = ChartRow(row_data, '', '')
        rows.append(row)

    return ChartEntity(columns, rows)


def get_visual_form_entity():
    field_info = get_field_info()
    field_options = []
    x_field_func_map = {}
    y_field_func_map ={}
    for info in field_info:
        x_field_func_map[info['name']] = get_x_avail_func(info['type'])
        y_field_func_map[info['name']] = get_y_avail_func(info['type'])
        field_options.append(FormOption(info['name'], info['name']))
    return VisualFormEntity(field_options, x_field_func_map, y_field_func_map)


def get_x_avail_func(fieldType):
    if (fieldType == "CharField"):
        return [FormOption("do nothing", "do_nothing")]
    elif (fieldType == "DateField"):
        return [ FormOption("month", "date_to_month"), FormOption("year", "date_to_year"), FormOption("month_year", "date_to_month_year")]
    elif (fieldType == "DecimalField" or fieldType == "IntegerField"):
        return [FormOption("do nothing", "do_nothing")]
    else:
        return [FormOption("do nothing", "do_nothing")]

def get_y_avail_func(fieldType):
    if (fieldType == "CharField"):
        return [FormOption("count", "count_frequency")]
    elif (fieldType == "DateField"):
        return [FormOption("do nothing", "do_nothing")]
    elif (fieldType == "DecimalField" or fieldType == "IntegerField"):
        return [FormOption("sum", "sum_by_group")]
    else:
        return [FormOption("process nothing", "process_nothing")]


def get_field_info():
    return [
        {
            'name': f.name,
            'type': str(f.get_internal_type())
        }
        for f in SuperStore._meta.fields if f.name is not 'id']

