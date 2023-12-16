def get_val(collection, key, default='git'):
    if not collection.get(key):
        return default
    else:
        return collection.get(key)
