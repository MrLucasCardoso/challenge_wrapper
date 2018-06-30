from challenge_wrapper import Api
from random import randint


def test_get_quotes():
    """
    Checking if method get_quotes is quering the API and returns a python 
    dictionary containing all quotes available
    """
    result = Api.get_quotes()

    # Checking of type
    assert type(result) is dict

    # Checking if quotes key exists in result
    assert 'quotes' in result

    # Checking if result is empty
    assert len(result['quotes']) > 0

    # Checking of all items are string
    assert all(type(_) is str for _ in result['quotes'])


def test_get_quote():
    """
    Checking if method get_quote(quote_number) is quering the API and 
    returns a python dictionary containing the corresponding quote
    """
    quote_number = randint(0, 10)  # Choosing a random number between 0 and 10
    result = Api.get_quote(quote_number)

    # Checking of type
    assert type(result) is dict

    # Checking if quote key exists in result
    assert 'quote' in result

    # Checking of type
    assert type(result['quote']) is str
