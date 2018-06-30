# Challenge_wrapper
This library will act as a wrapper around the API for a challenge

# Installation

## Prerequisites

- Python version 3.4, 3.5 or 3.6

```bash
$ pip install -e git+git@github.com:MrLucasCardoso/challenge_wrapper.git#egg=challenge_wrapper
```

# Usage

```python
from challenge_wrapper import Api

result_quotes = Api.get_quotes()
print(result_quotes['quotes'])

quote_number = 2
result_quote = Api.get_quote(quote_number)
print(result_quote['quote'])
```
