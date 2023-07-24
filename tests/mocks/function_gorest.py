import json
from typing import Any, Dict, List

from requests import Response

def mock_user_details_success(*args: List[Any], **kwargs: Dict[str, Any]):
    """Mock for response success."""
    result = {'id': 12345, 'name': 'Aishwarya', 'email': 'aisshwarya@test.com', 'gender': 'female', 'status': 'active'}     
    
    response = Response()
    response.status_code = 200
    response._content = bytes(json.dumps(result),encoding="utf-8")
    
    return response

def mock_user_list_success(*args: List[Any], **kwargs: Dict[str, Any]):
    """Mock for response success."""
    result = [{'id': 12345, 'name': 'Aishwarya', 'email': 'aisshwarya@test.com', 'gender': 'female', 'status': 'active'}]
    
    response = Response()
    response.status_code = 200
    response._content = bytes(json.dumps(result),encoding="utf-8")
    
    return response

def mock_user_details_failure(*args: List[Any], **kwargs: Dict[str, Any]) -> Response:
    """Mock for authentication error."""
    result = {
        "Error": "Invalid Authentication"
    }

    response = Response()
    response.status_code = 403
    response._content = bytes(json.dumps(result), encoding="utf-8")
    return response

def mock_user_list_failure(*args: List[Any], **kwargs: Dict[str, Any]) -> Response:
    """Mock for authentication error."""
    result = [{
        "Error": "Invalid Authentication"
    }]

    response = Response()
    response.status_code = 403
    response._content = bytes(json.dumps(result), encoding="utf-8")
    return response