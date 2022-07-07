try:
    import ujson as json
except ImportError:
    import json

import redis
from flask import g

config = json.load(open('config.json'))

REDIS_PASSWORD = config.get('redis_password', '')
REDIS_ADDRESS = config.get('redis_address', 'localhost')
REDIS_PORT = config.get('redis_port', 6379)
REDIS_DB = config.get('redis_db', 1)

def get_redis():
    if 'redis' not in g:
        g.redis = redis.Redis(host=REDIS_ADDRESS, port=REDIS_PORT, db=REDIS_DB, decode_responses=True, password=REDIS_PASSWORD)
    return g.redis
