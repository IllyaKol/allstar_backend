from . import urls
from .settings import REDIS_PROCESSING_KEY


def update_token_cache():
    cache = dict()
    redis = urls.redis_connection
    for key in redis.scan_iter(match=f'{REDIS_PROCESSING_KEY}*'):
        cache[key.decode('utf-8')] = redis.get(key)
    return cache
