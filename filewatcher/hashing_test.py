from filewatcher import hashing


def test_hashing():
    assert hashing.hash_str("hello") == "5d41402abc4b2a76b9719d911017c592"
