from rest_framework import serializers

from main.models import Supplier, Network, Product


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        