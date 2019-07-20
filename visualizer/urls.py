from django.urls import path

from visualizer import views

urlpatterns = [
    path('import/', views.import_data),
]
