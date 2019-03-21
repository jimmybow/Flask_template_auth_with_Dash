from flask_caching import Cache

cache = Cache()

cache.config = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache-directory',
    'CACHE_THRESHOLD': 50  # should be equal to maximum number of active users
}