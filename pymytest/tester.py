import requests
import time

def test_api(url, method='GET', data=None):
    start_time = time.time()
    
    if method.upper() == 'GET':
        response = requests.get(url)
    elif method.upper() == 'POST':
        response = requests.post(url, json=data)
    elif method.upper() == 'PUT':
        response = requests.put(url, json=data)
    elif method.upper() == 'DELETE':
        response = requests.delete(url)
    else:
        raise ValueError("Invalid HTTP method. Supported methods are GET, POST, PUT, and DELETE.")

    end_time = time.time()

    status_code = response.status_code
    body = response.text
    execution_time = end_time - start_time

    return status_code, body, execution_time
