from rest_framework import viewsets, status
from rest_framework.response import Response
from core.application.use_cases.category_use_cases import CategoryUseCases
from ..serializers.category_serializer import CategorySerializer
from core.infrastructure.cache.redis_cache_service import RedisCacheService
from core.infrastructure.django.repositories.category_repository import DjangoCategoryRepository

class CategoryViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_cases = CategoryUseCases(
            repository=DjangoCategoryRepository(),
            cache_service=RedisCacheService()
        )

    def list(self, request):
        categories = self.use_cases.get_all_categories()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        category = self.use_cases.get_category(pk)
        if not category:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = self.use_cases.create_category(serializer.to_dto())
        return Response(CategorySerializer(category).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category_dto = serializer.to_dto()
        category_dto.id = pk
        category = self.use_cases.update_category(category_dto)
        return Response(CategorySerializer(category).data)

    def destroy(self, request, pk=None):
        self.use_cases.delete_category(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)