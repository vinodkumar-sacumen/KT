from src.demo1 import fetch
import pytest


def test_fetch():
    response = fetch(url="https://api.publicapis.org/entries")
    data = response.json()
    assert response.status_code == 200
    assert data["count"] == 1425
