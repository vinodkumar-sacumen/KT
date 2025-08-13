"""Mocks"""
import json
from typing import Any, Dict, List

from requests import Response


def mock_api_success(*args: List[Any], **kwargs: Dict[str, Any]) -> Response:
    """Mock for response success."""
    result = {
        "count":1425,
        "entries":[
            {
                "API":"AdoptAPet",
                "Description":"Resource to help get pets adopted",
                "Auth":"apiKey",
                "HTTPS":True,
                "Cors":"yes",
                "Link":"https://www.adoptapet.com/public/apis/pet_list.html",
                "Category":"Animals"
            }
        ]
    }
    url = "https://api.publicapis.org/entries"

    response = Response()
    response.status_code = 200
    response.url = url
    response._content = bytes(json.dumps(result), encoding="utf-8")
    return response


def mock_api_failure(*args: List[Any], **kwargs: Dict[str, Any]) -> Response:
    """Mock for authentication error."""
    result = {
        "Error": "Invalid Authentication"
    }

    response = Response()
    response.status_code = 403
    response._content = bytes(json.dumps(result), encoding="utf-8")
    return response
