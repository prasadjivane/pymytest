"""Module for testing APIs."""

import time
import requests


def test_api(url, method="GET", data=None):
    """
    Test an API and return response status code, body, and execution time.

    :param url: The URL of the API to test.
    :param method: The HTTP method to use (default is "GET").
    :param data: The data to send with the request (for POST and PUT methods).
    :return: A tuple containing the status code, response body, and execution time.
    """
    start_time = time.time()
    if method.upper() == "GET":
        response = requests.get(url, timeout=10)
    elif method.upper() == "POST":
        response = requests.post(url, json=data, timeout=10)
    elif method.upper() == "PUT":
        response = requests.put(url, json=data, timeout=10)
    elif method.upper() == "DELETE":
        response = requests.delete(url, timeout=10)

    else:
        raise ValueError("Invalid methods are GET, POST, PUT, and DELETE.")

    end_time = time.time()

    status_code = response.status_code
    body = response.text
    execution_time = end_time - start_time

    return status_code, body, execution_time
