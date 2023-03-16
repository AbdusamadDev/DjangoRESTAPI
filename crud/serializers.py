from rest_framework import serializers
from .models import ProductModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = [
            "name",
            "content",
            "price",
        ]
