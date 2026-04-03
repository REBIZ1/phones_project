from django.urls import path
from phones.views import catalog, product_detail

urlpatterns = [
    path('catalog/', catalog, name='catalog'),
    path('catalog/<slug:slug>/', product_detail, name='product_detail'),
]