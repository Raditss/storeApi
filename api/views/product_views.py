from rest_framework import viewsets, status
from rest_framework.response import Response
from core.application.use_cases.product_use_cases import ProductUseCases
from ..serializers.product_serializer import ProductSerializer
from ..filters.product_filter import ProductFilterSerializer
from core.infrastructure.cache.redis_cache_service import RedisCacheService
from core.infrastructure.django.repositories.product_repository import DjangoProductRepository

class ProductViewSet(viewsets.ViewSet):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.use_cases = ProductUseCases(
            repository=DjangoProductRepository(),
            cache_service=RedisCacheService()
        )

    def list(self, request):
        filter_serializer = ProductFilterSerializer(data=request.query_params)
        filter_serializer.is_valid(raise_exception=True)
        products = self.use_cases.get_all_products(
            category=filter_serializer.validated_data.get('category'),
            price_min=filter_serializer.validated_data.get('price_min'),
            price_max=filter_serializer.validated_data.get('price_max')
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        product = self.use_cases.get_product(pk)
        if not product:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = self.use_cases.create_product(serializer.to_dto())
        return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product_dto = serializer.to_dto()
        product_dto.id = pk
        product = self.use_cases.update_product(product_dto)
        return Response(ProductSerializer(product).data)

    def destroy(self, request, pk=None):
        self.use_cases.delete_product(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)