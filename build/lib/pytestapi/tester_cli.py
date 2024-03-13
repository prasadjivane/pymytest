import argparse
from .tester import test_api

def main():
    parser = argparse.ArgumentParser(description='Test an API and return response status code, body, and execution time.')
    parser.add_argument('url', type=str, help='URL of the API to test')

    args = parser.parse_args()
    url = args.url

    status_code, body, execution_time = test_api(url)

    print(f"Status Code: {status_code}")
    print(f"Response Body: {body}")
    print(f"Execution Time: {execution_time} seconds")

if __name__ == "__main__":
    main()
