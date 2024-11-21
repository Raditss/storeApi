from typing import List, Optional
from decimal import Decimal
from ..dto.product_dto import ProductDTO
from ...domain.interfaces.product_repository import ProductRepository
from ...domain.filter.filter import ProductFilter
from ..interface.cache_service import CacheService

class ProductUseCases:
    def __init__(self, repository: ProductRepository, cache_service: CacheService):
        self._repository = repository
        self._cache_service = cache_service
        self._cache_key = "store:products"

    def get_all_products(self, category: Optional[str] = None, price_min: Optional[Decimal] = None, price_max: Optional[Decimal] = None) -> List[ProductDTO]:
        # Create filter specification
        filter_spec = None
        if any([category, price_min, price_max]):
            filter_spec = ProductFilter(
                category=category,
                price_min=price_min,
                price_max=price_max
            )
            # Don't use cache for filtered results
            return self._repository.get_all(filter_spec)
        
        # Use cache for unfiltered results
        cached_products = self._cache_service.get(self._cache_key)
        if cached_products:
            return cached_products

        products = self._repository.get_all()
        self._cache_service.set(self._cache_key, products)
        return products

    def get_product(self, product_id: int) -> ProductDTO:
        return self._repository.get_by_id(product_id)

    def create_product(self, product_dto: ProductDTO) -> ProductDTO:
        product = self._repository.create(product_dto)
        self._cache_service.delete(self._cache_key)
        # return product

    def update_product(self, product_dto: ProductDTO) -> ProductDTO:
        product = self._repository.update(product_dto)
        self._cache_service.delete(self._cache_key)
        return product

    def delete_product(self, product_id: int) -> None:
        self._repository.delete(product_id)
        self._cache_service.delete(self._cache_key)