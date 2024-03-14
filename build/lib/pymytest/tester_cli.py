"""CLI for testing APIs."""

import argparse
import json

import requests
from .tester import test_api


def main():
    """
    Main function to parse command-line arguments and execute API test.
    """
    parser = argparse.ArgumentParser(
        description="return status code, body, and execution time."
    )
    parser.add_argument(
        "method",
        type=str,
        choices=["GET", "POST", "PUT", "DELETE"],
        help="HTTP method (GET, POST, PUT, DELETE)",
    )
    parser.add_argument("url", type=str, help="URL of the API to test")
    parser.add_argument(
        "data",
        type=str,
        nargs="?",
        default=None,
        help="Data to include in the request (for POST and PUT methods)",
    )

    args = parser.parse_args()
    method = args.method
    url = args.url
    data = args.data

    if data:
        try:
            data = json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Error: Invalid JSON data format: {e}")
            return

    try:
        status_code, body, execution_time = test_api(url, method, data)
        print(f"Status Code: {status_code}")
        print(f"Response Body: {body}")
        print(f"Execution Time: {execution_time:.4f} seconds")
    except requests.RequestException as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
