"""Conftest File."""

import pytest
from typing import Dict, Any

FILTER_VALUE = "REDACTED"


@pytest.fixture(scope="module")
def vcr_config() -> Dict[Any, Any]:
    """Vcr config method.

    Returns:
        Dict: dictionary of configuration.
    """
    return {
        "filter_headers": [("authorization", FILTER_VALUE)],
        "filter_query_parameters": [
            ("client_id"),
            FILTER_VALUE,
            ("refresh_token", FILTER_VALUE),
            ("access_token", FILTER_VALUE),
            ("code", FILTER_VALUE),
        ],
        "filter_post_data_parameters": [
            ("client_secret", FILTER_VALUE),
            ("client_id", FILTER_VALUE),
            ("code", FILTER_VALUE),
            ("refresh_token", FILTER_VALUE),
            ("access_token", FILTER_VALUE),
        ],
        "record_mode": "none",
    }
