import argparse
from .tester import test_api

def main():
    parser = argparse.ArgumentParser(description='Test an API and return response status code, body, and execution time.')
    parser.add_argument('method', type=str, choices=['GET', 'POST', 'PUT', 'DELETE'], help='HTTP method (GET, POST, PUT, DELETE)')
    parser.add_argument('url', type=str, help='URL of the API to test')
    parser.add_argument('data', type=str, nargs='?', default=None, help='Data to include in the request (for POST and PUT methods)')

    args = parser.parse_args()
    method = args.method
    url = args.url
    data = args.data

    if data:
        try:
            data = eval(data)
        except Exception as e:
            print(f"Error: Invalid data format: {e}")
            return

    status_code, body, execution_time = test_api(url, method, data)

    print(f"Status Code: {status_code}")
    print(f"Response Body: {body}")
    print(f"Execution Time: {execution_time:.4f} seconds")

if __name__ == "__main__":
    main()
