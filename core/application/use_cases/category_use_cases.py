from typing import List
from ..dto.category_dto import CategoryDTO
from ...domain.interfaces.category_repository import CategoryRepository
from ..interface.cache_service import CacheService

class CategoryUseCases:
    def __init__(self, repository: CategoryRepository, cache_service: CacheService):
        self._repository = repository
        self._cache_service = cache_service
        self._cache_key = "store:categories"

    def get_all_categories(self) -> List[CategoryDTO]:
        cached_categories = self._cache_service.get(self._cache_key)
        if cached_categories:
            return cached_categories

        categories = self._repository.get_all()
        self._cache_service.set(self._cache_key, categories)
        return categories

    def get_category(self, category_id: int) -> CategoryDTO:
        return self._repository.get_by_id(category_id)

    def create_category(self, category_dto: CategoryDTO) -> CategoryDTO:
        category = self._repository.create(category_dto)
        self._cache_service.delete(self._cache_key)
        return category

    def update_category(self, category_dto: CategoryDTO) -> CategoryDTO:
        category = self._repository.update(category_dto)
        self._cache_service.delete(self._cache_key)
        return category

    def delete_category(self, category_id: int) -> None:
        self._repository.delete(category_id)
        self._cache_service.delete(self._cache_key)