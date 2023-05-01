# Asapp-Lead-SDET-Challenge-API

<p align="center">
  <img src="images/logo.PNG" width="400" height="250"/>
</p>

## Description

Asapp-Lead-SDET-Challenge-API was developed using Python, Pytest and Request library.

## Languages, libraries and tools used

* __[Python](https://www.python.org/downloads/)__
* __[Pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)__
* __[Requests](https://docs.python-requests.org/en/master/)__
* __[Pycharm](https://www.jetbrains.com/pycharm/download/)__

Above Features are used to make code simple, generic, understandable, clean and easily maintainable for future development.

## Installation

Install the dependencies and start the testing.

 __Install Pytest__:
```sh
pip install -U pytest
```
 __Install Requests__:
```sh
pip install requests
```

## Automated tests

### Run Docker

Precondition: you need to have downloaded the "ASAPP - QA Automation Challenge" docker image.

```bash
# Build the Images for API and UI:

docker build ./src/api -t asapp-qa-challenge-api

docker build ./src/ui -t asapp-qa-challenge-ui

# Start them through docker-compose:

docker-compose up -d

Browse to localhost:3000 to access the challenge UI.

Browse to localhost:5000/api/docs/ for the API spec.

Command above will run the containers in background, but you can always follow logs with docker-compose logs -f.

To stop containers you can run docker-compose stop.
```

__To run a test, you can simply write the following command on Terminal__:
```sh
pytest
```

__To run and get details of all the executed test, you can simply write the following command on Terminal__:
```sh
pytest -rA
```

# Prerequisites
* __Python__
* __Any IDE__

# Built With

* __[Python](https://www.python.org/downloads/)__ - Language used to build the application.
* __[Pycharm](https://www.jetbrains.com/pycharm/download/)__ - The IDE for writing Automation Test Scripts
