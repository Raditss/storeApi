from rest_framework import serializers
from core.application.dto.product_dto import ProductDTO

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_null=True, required=False)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    category_id = serializers.IntegerField()

    def to_dto(self) -> ProductDTO:
        return ProductDTO(**self.validated_data)
