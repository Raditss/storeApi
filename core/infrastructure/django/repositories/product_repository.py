from typing import List, Optional
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from ....domain.interfaces.product_repository import ProductRepository
from ....domain.entities.product import Product
from ....domain.filter.filter import ProductFilter
from ..models import ProductModel

class DjangoProductRepository(ProductRepository):
    def get_all(self, filters: Optional[ProductFilter] = None) -> List[Product]:
        queryset = ProductModel.objects.all()
        if filters:
            filter_conditions = Q()  # Use a different variable name
            if filters.category is not None:
                filter_conditions &= Q(category__name__iexact=filters.category)
            if filters.price_min is not None:
                filter_conditions &= Q(price__gte=filters.price_min)
            if filters.price_max is not None:
                filter_conditions &= Q(price__lte=filters.price_max)
            queryset = queryset.filter(filter_conditions)
        return [self._to_entity(product) for product in queryset]
    
    def get_by_id(self, product_id: int) -> Optional[Product]:
        try:
            product = ProductModel.objects.get(id=product_id)
            return self._to_entity(product)
        except ObjectDoesNotExist:
            return None

    def create(self, product: Product) -> Product:
        model = ProductModel(
            name=product.name,
            description=product.description,
            price=product.price,
            category_id=product.category_id
        )
        model.save()
        return self._to_entity(model)

    def update(self, product: Product) -> Product:
        model = ProductModel.objects.get(id=product.id)
        model.name = product.name
        model.description = product.description
        model.price = product.price
        model.category_id = product.category_id
        model.save()
        return self._to_entity(model)

    def delete(self, product_id: int) -> None:
        ProductModel.objects.filter(id=product_id).delete()

    def _to_entity(self, model: ProductModel) -> Product:
        return Product(
            id=model.id,
            name=model.name,
            description=model.description,
            price=model.price,
            category_id=model.category_id
       )