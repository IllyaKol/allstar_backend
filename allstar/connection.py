import redis

from .settings import REDIS_SETTINGS


def init_connections():
    redis_connection = redis.StrictRedis(
        host=REDIS_SETTINGS['host'],
        port=REDIS_SETTINGS['port'],
        db=REDIS_SETTINGS['db']
    )

    return redis_connection
