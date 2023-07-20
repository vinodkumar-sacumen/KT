import json
from typing import Any, Dict, List

from requests import Response

def mock_user_details_success(*args: List[Any], **kwargs: Dict[str, Any]):
    """Mock for response success."""
    result = {'id': 3786877, 'name': 'Sen. Aishani Nambeesan', 'email': 'aishani_sen_nambeesan@sporer-gottlieb.test', 'gender': 'female', 'status': 'active'}     
    
    response = Response()
    response.status_code = 200
    response._content = bytes(json.dumps(result),encoding="utf-8")
    
    return response

def mock_user_list_success(*args: List[Any], **kwargs: Dict[str, Any]):
    """Mock for response success."""
    result = [{'id': 3786877, 'name': 'Sen. Aishani Nambeesan', 'email': 'aishani_sen_nambeesan@sporer-gottlieb.test', 'gender': 'female', 'status': 'active'}]
    
    response = Response()
    response.status_code = 200
    response._content = bytes(json.dumps(result),encoding="utf-8")
    
    return response
