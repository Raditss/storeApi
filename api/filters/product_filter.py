from rest_framework import serializers
from decimal import Decimal
from typing import Optional

class ProductFilterSerializer(serializers.Serializer):
    category = serializers.CharField(required=False)
    price_min = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    price_max = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    def validate(self, data):
        price_min = data.get('price_min')
        price_max = data.get('price_max')

        if price_min and price_max and price_min > price_max:
            raise serializers.ValidationError(
                "price_min cannot be greater than price_max"
            )
        return data