### Run cloud-build-local
```bash
$ cloud-build-local --dryrun=false .
$ cloud-build-local --dryrun=false --substitutions=_GIT_USERNAME="username",_GIT_PASSWORD="password" .
```

### Run Tests
```bash
$ pytest tests/
```

### Run test with coverage
```bash
$ pytest --cov-report term-missing --cov
```

### Run pylint
```bash
$ pylint <filename or directoryname>
$ pylint models/ tests/
```

### Generate docs
- To add a new module add the following to the **index.rst** file:
```dotenv
.. automodule:: models.car
    :members:
```
- generate docs with the following
```bash
$ cd docs
$ make html
```

### ToDo
- [] constructor param default value
