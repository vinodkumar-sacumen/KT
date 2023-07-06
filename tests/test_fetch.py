import pytest
import logging
import requests
import pytest_mock
from unittest import mock
from src.fetch import fetch

    
def test_fetch():
    url = "https://api.publicapis.org/entries"
    logging.basicConfig(level=logging.DEBUG)
    log_messages = []
    
    def log_error(msg):
        log_messages.append(msg)
    logging.debug = log_error
    result = fetch(url)
    assert result is not None
    
    with open("fetched.log",'w') as log_file:
        log_file.write("\n".join(log_messages))    
 
    
    
