from django.core.cache import cache
from ...application.interface.cache_service import CacheService

class RedisCacheService(CacheService):
    def get(self, key: str):
        return cache.get(key)

    def set(self, key: str, value, timeout=None):
        cache.set(key, value, timeout)

    def delete(self, key: str):
        cache.delete(key)