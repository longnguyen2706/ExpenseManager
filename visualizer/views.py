from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from visualizer.models import SuperStore
from visualizer.services import group_by, date_to_year, sum_by_group


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
    values, gr_records = group_by('order_date', date_to_year,  SuperStore.objects.all())
    print (values)
    print( sum_by_group('quantity', gr_records))
