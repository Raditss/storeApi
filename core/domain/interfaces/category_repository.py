from abc import ABC, abstractmethod
from typing import List, Optional
from ..entities.category import Category

class CategoryRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Category]:
        pass

    @abstractmethod
    def get_by_id(self, category_id: int) -> Optional[Category]:
        pass

    @abstractmethod
    def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, category_id: int) -> None:
        pass