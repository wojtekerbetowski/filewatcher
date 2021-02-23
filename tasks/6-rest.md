Expose the filewatching functionality in a form of a HTTP JSON API, with the following endpoints:

```
GET /snapshots/{snapshot_path}/verify?directory={dir}

POST /snapshots/{snapshot_path}/store
body(json): {"directory": "{dir}"}
```

Steps:

* [ ] Install `flask` library
* [ ] Add the `api` module to implement these endpoints
* [ ] Write unit and integration tests to cover the requirements
* [ ] Implement the function and make sure all tests pass
