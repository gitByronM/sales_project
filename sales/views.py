from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Sale
from .serializers import SaleSerializer

class SaleCreateView(generics.CreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer   

class SaleListView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['product_name', 'product_code', 'product_category', 'sale_date']
    ordering_fields = ['sale_date', 'unit_price', 'quantity_sold']  # Agregar los campos de ordenamiento
    ordering = ['sale_date']  # Orden por defecto
    search_fields = ['product_name', 'product_code']  # Campos en los que se puede buscar

