Add a module `snapshot_repository` with the following functions:

```
def store(path: Path, data: Dict[str, str]) -> str:
    pass

def load(path: Path) -> data: Dict[str, str]:
    pass
```

which is used to persist and load hashes of a directory in a flat structure.

Steps:

* [ ] Add a module with the function signatures
* [ ] Write unit tests to cover the requirements
* [ ] Implement the functions and make sure all tests pass

Suggestion: use `json` module to serialize the data.
