def hash_str(content):
    import hashlib
    return hashlib.md5(content.encode()).hexdigest()
