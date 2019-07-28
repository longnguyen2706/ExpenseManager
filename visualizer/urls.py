from django.urls import path

from visualizer import views

urlpatterns = [
    path('import/', views.import_data),
    path ('sales-by-year/', views.sales_by_year),
    path ('quantity-by-month/', views.quantity_by_month),
    path ('all-records/', views.get_all_records),
    path ('processing-form/', views.get_processing_form),
    path ('plot-chart/', views.plot_chart)
]
