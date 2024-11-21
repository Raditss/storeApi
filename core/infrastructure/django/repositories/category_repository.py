from typing import List, Optional
from django.core.exceptions import ObjectDoesNotExist
from ....domain.interfaces.category_repository import CategoryRepository
from ....domain.entities.category import Category
from ..models import CategoryModel

class DjangoCategoryRepository(CategoryRepository):
    def get_all(self) -> List[Category]:
        categories = CategoryModel.objects.all()
        return [self._to_entity(category) for category in categories]

    def get_by_id(self, category_id: int) -> Optional[Category]:
        try:
            category = CategoryModel.objects.get(id=category_id)
            return self._to_entity(category)
        except ObjectDoesNotExist:
            return None

    def create(self, category: Category) -> Category:
        model = CategoryModel(
            name=category.name,
            description=category.description
        )
        model.save()
        return self._to_entity(model)

    def update(self, category: Category) -> Category:
        model = CategoryModel.objects.get(id=category.id)
        model.name = category.name
        model.description = category.description
        model.save()
        return self._to_entity(model)

    def delete(self, category_id: int) -> None:
        CategoryModel.objects.filter(id=category_id).delete()

    def _to_entity(self, model: CategoryModel) -> Category:
        return Category(
            id=model.id,
            name=model.name,
            description=model.description
        )
