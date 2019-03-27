def hash_str(content: str) -> str:
    """Creates an MD5 checksum of a `content` string"""

    import hashlib

    return hashlib.md5(content.encode()).hexdigest()
