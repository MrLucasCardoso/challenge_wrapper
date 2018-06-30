from challenge_wrapper import Api


def test_get_quotes():
    """
    Checking if method get_quotes is quering the API and returns a python 
    dictionary containing all quotes available
    """
    quotes = Api.get_quotes()

    # Checking of type
    assert type(quotes) is dict

    # Checking if result is empty
    assert len(quotes) > 0

    # Checking of all items are string
    assert all(type(_) is str for _ in quotes)
    
    
def test_get_quote():
    pass

