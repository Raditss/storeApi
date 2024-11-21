from rest_framework import serializers
from core.application.dto.category_dto import CategoryDTO

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_null=True, required=False)

    def to_dto(self) -> CategoryDTO:
        return CategoryDTO(
            id=getattr(self.instance, 'id', None),
            **self.validated_data
        )