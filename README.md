[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/andrewmkrug/sample_jsonplaceholder)

# Features

* Parallelized Tests
* Random Order Execution
* DotEnv file for different testing environments 
* Response status codes for easier determination of server errors
* Pydantic for models with validators
* GitPod config for virtual coding space

# Setup

Requirements:
* Python 3.8
* Pipenv

`pipenv install`
`pipenv run pytest`

## Windows Issues

Windows users can't use `--workers auto` in the `pytest.ini` pickling doesnt work on Windows and the pytest-parallel package

# Issues with Prod JSONPlaceHolder 

Changing data, POST, PUT, DELETE doesn't work in the production env

# Features to Add

Access to models and API unit tests, mainly to see what is there and what should I look into adding support for.

* **[Report Portal](https://reportportal.io)**: To track overall changes to and stability of test suite, growth 
* **[Hypothesis](https://hypothesis.readthedocs.io/en/latest/index.html)** Properties Based Testing
    * need to study up on the package and implement appx 8 hours unless implemented in unit tests
* Better Mocks or Mock service with JSON PlaceHolder running locally





