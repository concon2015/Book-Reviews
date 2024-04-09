# Chapter 11

## Installing Modules

Modules can be installed by using `pip` or `python -m pip`

Example: `python -m pip install pytest`

## Testing Functions

You can use pytest to test functions

 - Test files need to import the desired functions
 - Test files need to begin with 'test_'
 - Test functions need to begin with 'test_'
 - Test functions need to end with `assert value = 'expected result'`

 You can run pytest by running `python -m pytest` which will run all tests found within the current directory

Example:

 ```
from name_function import get_formatted_name

def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
 ```

 ## Testing Classes

 You can create a fixture to build a class that is repeatable across multiple test functions

 You create a fixture by adding `@pytest.fixture` above the function that creates the class

 Following the class creation, you have to return the class and pass the name of the function as a parameter to each testing function

 Example:

 ```
import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """A survey that will be available to all test functions."""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """Test that a single response is stored properly."""
    language_survey.store_response('English')
    assert 'English' in language_survey.responses
 ```