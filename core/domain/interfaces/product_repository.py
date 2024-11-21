from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.product import Product
from ..filter.filter import ProductFilter

class ProductRepository(ABC):
    @abstractmethod
    def get_all(self, filter_spec: Optional[ProductFilter] = None) -> List[Product]:
        pass

    @abstractmethod
    def get_by_id(self, product_id: int) -> Optional[Product]:
        pass

    @abstractmethod
    def create(self, product: Product) -> Product:
        pass

    @abstractmethod
    def update(self, product: Product) -> Product:
        pass

    @abstractmethod
    def delete(self, product_id: int) -> None:
        pass