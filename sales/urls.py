from django.urls import path
from .views import SaleCreateView, SaleListView

urlpatterns = [
    path('sales/create/', SaleCreateView.as_view(), name='sale-create'),
    path('sales/', SaleListView.as_view(), name='sale-list'),
]
