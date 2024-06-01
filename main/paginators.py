from rest_framework.pagination import PageNumberPagination


class SupplyChainPaginator(PageNumberPagination):
    page_size = 5
