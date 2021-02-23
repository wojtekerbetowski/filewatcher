Expose the filewatching functionality in a form of a CLI, with the following usage:

```
$ python cli.py # prints help
...

$ python cli.py save dir --snapshot=data.json
...

$ python cli.py verify dir --snapshot=data.json 
...
```

Steps:

* [ ] Install `click` library
* [ ] Add a CLI module with the commands
* [ ] Write unit and integration tests to cover the requirements
* [ ] Implement the function and make sure all tests pass
* [ ] Optional (Create an executable `filewatcher`)
