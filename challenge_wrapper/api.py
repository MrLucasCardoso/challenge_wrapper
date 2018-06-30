from python_http_client import Client # I already use this lib in other projects
from python_http_client.exceptions import HTTPError
from .settings import BASE_URL

class Api:
    """
    Class that provides the methods for the Challenge API
    """

    @classmethod
    def _get_client(cls):
        """Method for create a client http"""
        return Client(host=BASE_URL, append_slash=False)

    @classmethod
    def get_quotes(cls, raise_exception=False):
        """
        Queries the API and returns a dictionary containing all 
        quotes available.
        If occured any error in request, returns a dict with empty quote list
        :param: raise_exception: Flag that if true raises the exception, 
        and if not it returns the dictionary with the empty quotes 
        list. By default it is False
        :return: Dictionary with the following items: { 'quotes': ['', '', ...] }
        """
        client = cls._get_client()
        try:
            response = client.quotes.get()
            return response.to_dict
        except HTTPError as err:
            if raise_exception:
                raise err
            return {'quotes': []}


