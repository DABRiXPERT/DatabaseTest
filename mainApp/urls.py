from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-number/', views.add_number, name='add_number'),
    path('show-content/', views.show_content, name='show_content'),
    path('calculate-sum/', views.calculate_sum, name='calculate_sum'),
]
