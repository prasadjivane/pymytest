import requests
import time

def test_api(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()

    status_code = response.status_code
    body = response.text
    execution_time = end_time - start_time

    return status_code, body, execution_time
