import pytest
import logging
import requests
from unittest import mock
from src.fetch import fetch


def test_fetch(caplog):
    url = "https://api.publicapis.org/entries"
    caplog.set_level(logging.ERROR)
    result = fetch(url)
    assert result is not None
    assert len(caplog.records)==0
    caplog.handler.stream.close()
    
    
