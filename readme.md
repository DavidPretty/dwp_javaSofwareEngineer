# DWP Associate Java Software Engineer Application-David Pretty

This is my submission for the online test. This a very simple API, with one method-GET and one endpoint. The API was built in Python 2.7 using Flask, as Flask can build an API with very little overhead. The API calls the provided test API and returns a list of people who either:
1. Live in London-I took this to mean the users returned by https://bpdts-test-app.herokuapp.com/city/London/users
2. Are within 50 miles of London. I took this to mean their location was within 50 miles of the centre of London. I took Trafalgar Square to be the centre of London, as conventionally this is where [distances to London are measured from][0] and used the [Haversine formula][1] to calculate the distances.

### Prerequisites

You need Python 2.7.12 and Flask 1.1.1

### Installing

The 2 files, flask_app.py & test_flask_app.py, for the code and the tests, can be installed in the root directory of a Flask project. This would not be the best structure for a more elaborate API but I hope it is sufficient for this test.

The API is online at http://thistledown.pythonanywhere.com

## Running the tests

The tests are are all contained in test_flask_app.py and can be invoked by running pytest from the command line.

## Possible Improvements
* The API does not deal with the helper API failing, it could be amended so it returns a 500 response if this occurs.
* The tests invoke methods that call the helper API. This makes them dependent on the helper API and means the tests cannot model the failure of the helper API. This could be improved by mocking the helper API, which would remove that dependency from testing and allow testing of how the API handles the failure of the helper API.

## Built With

* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Flask 1.1.1](https://flask.palletsprojects.com/en/1.1.x/) - Web Framework used
* [PythonAnywhere](https://www.pythonanywhere.com/)-online Python development environment


## Author

* **David Pretty**

[0]: https://en.wikipedia.org/wiki/Central_London
[1]: https://en.wikipedia.org/wiki/Haversine_formula

