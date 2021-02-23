Add a module `filewatcher` in the `filewatcher` package, that exposes the core functionality:

```
def save(directory: Path, snapshot: Path) -> None:
    "Saves a snapshot with the hashed contents to the disk"

def verify(directory: Path, snapshot: Path) -> None:
    "Loads the stored snapshot and verifies whether files changed"
```

Steps:

* [ ] Add a module with the functions signatures 
* [ ] Write unit tests to cover the requirements
* [ ] Implement the function and make sure all tests pass
* [ ] (Optional) Mock other modules to only cover this module's logic
