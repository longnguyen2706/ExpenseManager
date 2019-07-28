import json

from django.core import serializers
from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render

from visualizer.ProcessingFunction import ProcessingFunction
from visualizer.entities import *
from visualizer.models import SuperStore
from visualizer.services import *
from django.views.decorators.csrf import csrf_exempt

pros_func = ProcessingFunction()

def import_data(request):
    SUPER_STORE_FILE = "../resources/sample_superstore.xls"
    import pandas as pd
    from FileManipulation.read_util import filter_by_cols, get_file_in_resource
    excel_path = get_file_in_resource(SUPER_STORE_FILE)
    # open_xls_as_xlsx(file_path)
    df = pd.read_excel(excel_path, sheet_name="Orders", header=0)
    super_stores = []
    for row in df.iterrows():
        s = SuperStore(order_id=row[1]['Order ID'], order_date=row[1]['Order Date'], ship_date= row[1]['Ship Date'],
                       ship_mode=row[1]['Ship Mode'], customer_id=row[1]['Customer ID'], customer_name=row[1]['Customer Name'],
                       segment=row[1]['Segment'], country=row[1]['Country'], city = row[1]['City'], state = row[1]['State'],
                       postal_code=row[1]['Postal Code'], region=row[1]['Region'], product_id=row[1]['Product ID'],
                       category= row[1]['Category'], sub_category=row[1]['Sub-Category'], product_name=row[1]['Product Name'],
                       sales = row[1]['Sales'], quantity=row[1]['Quantity'], discount=row[1]['Discount'], profit=row[1]['Profit'])
        super_stores.append(s)

    SuperStore.objects.bulk_create(super_stores)
    # data = serializers.serialize("json", super_stores, indent=4)

    return HttpResponse("Inserted "+ str(len(super_stores)) + " records")


def sales_by_year(request):
    values, gr_records = group_by('order_date', pros_func.date_to_year,  SuperStore.objects.all())
    sums = pros_func.sum_by_group('quantity', gr_records)
    chart_entity = get_chart_entity(values, [sums])
    table_entity = get_table_entity(values, [sums])
    data = json.dumps(VisualizerEntity(chart_entity, table_entity), default = serialize)
    return HttpResponse(data, content_type='application/json')

def quantity_by_month(request):
    values, gr_records = group_by('sub_category', pros_func.do_nothing, SuperStore.objects.all())
    sums = pros_func.sum_by_group('profit', gr_records)
    chart_entity = get_chart_entity(values, [sums])
    table_entity = get_table_entity(values, [sums])
    data = json.dumps(VisualizerEntity(chart_entity, table_entity), default=serialize)
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def plot_chart(request):
    if request.method == 'POST':
        values=json.loads(request.body.decode('utf-8'))
        visual_entities = []
        for value in values:
            form_value = FormValue(value['xField'], value['xFunc'], value['yField'], value['yFunc'])
            values, gr_records = group_by(form_value.xField, getattr(pros_func, form_value.xFunc), SuperStore.objects.all())
            f = getattr(pros_func, form_value.yFunc)
            sums = f(form_value.yField, gr_records)
            chart_entity = get_chart_entity(values, [sums])
            table_entity = get_table_entity(values, [sums])
            visual_entities.append(VisualizerEntity(chart_entity, table_entity))
        data = json.dumps(visual_entities, default=serialize)
        return HttpResponse(data, content_type='application/json')

def get_all_records(request):
    records = SuperStore.objects.all()[:100]
    # dict_obj = model_to_dict(records)
    # data = json.dumps(dict_obj, default=serialize)
    cols = [f['name'] for f in get_field_info()]
    # r_data = [d['fields'] for d in serializers.serialize("json", records)]
    r_data = serializers.serialize("json", records)
    json_data = {
        'cols': cols,
        'records': json.loads(r_data)
    }
    return HttpResponse(json.dumps(json_data), content_type='application/json')

def get_processing_form(request):
    data = json.dumps(get_visual_form_entity(), default=serialize)
    return HttpResponse(data, content_type='application/json')
