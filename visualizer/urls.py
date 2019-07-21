from django.urls import path

from visualizer import views

urlpatterns = [
    path('import/', views.import_data),
    path ('sales-by-year/', views.sales_by_year)
]
