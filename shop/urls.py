from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.index),
    path('<int:product_id>', views.single_product, name="single_product")
]
