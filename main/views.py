from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from main.models import Supplier, Network, Product
from main.paginators import SupplyChainPaginator
from main.permissions import IsActive
from main.serializers import SupplierSerializer, NetworkSerializer, ProductSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    filter_backends = [SearchFilter]  # фильтр поиска по стране
    filterset_fields = ['country']
    pagination_class = SupplyChainPaginator
    permission_classes = [IsActive]

    def update(self, request, *args, **kwargs):
        """Запрещено обновление через API поля «Задолженность перед поставщиком»"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        if 'arrears' in serializer.validated_data:
            serializer.validated_data.pop('debt')
        self.perform_update(serializer)

        return Response(serializer.data)


class NetworkViewSet(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()
    pagination_class = SupplyChainPaginator
    permission_classes = [IsActive]


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    pagination_class = SupplyChainPaginator
    permission_classes = [IsActive]
