"""Python file that fetches user and user details api."""

from typing import List, Dict, Any

import requests

API_URL = "https://gorest.co.in/public/v2/users"
USER_DETAILS_API_URL = "https://gorest.co.in/public/v2/users/"


def fetch(user_api_url: str, details_api_url: str) -> List[Any]:
    """Fetch the user and user details from an API.

    Args:
        user_api_url (str): url of user list API
        details_api_url (str): url of user details API

    Returns:
        list: returns the list of user details
    """
    user_id_list = user_list(user_api_url)
    if user_id_list:
        user_details_list = user_details(details_api_url, user_id_list)
        return user_details_list
    return user_id_list


def user_list(url: str) -> List[int]:
    """Fetch user list from an API.

    Args:
        url (str): url of user list API

    Returns:
        list: returns list of user id
    """
    user_id_list: List[int] = []
    users = requests.get(
                            url=url,
                            headers={'Content-Type': 'application/json'},
                            timeout=20
                        )
    if users.status_code == 200:
        users_data = users.json()
    else:
        return user_id_list
    for user in users_data:
        user_id_list.append(user["id"])
    return user_id_list


def user_details(url: str, user_id_list: List[int]) -> List[Dict[Any, Any]]:
    """Fetch user details from an API based on list of user id.

    Args:
        url (str): url of user details API
        user_id_list (list): list of user ids

    Returns:
        list: returns list of user details
    """
    user_details_list: List[Dict[Any, Any]] = []
    for user_id in user_id_list:
        details = requests.get(
                                url=url + str(user_id),
                                headers={'Content-Type': 'application/json'},
                                timeout=20
                            )
        if details.status_code == 200:
            user_details_list.append(details.json())
        else:
            return user_details_list
    return user_details_list


response = fetch(API_URL, USER_DETAILS_API_URL)
print(response)
