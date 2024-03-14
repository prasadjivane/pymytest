<img width="700" alt="pymytest" src="https://github.com/prasadjivane/pymytest/assets/26869583/34f71b86-c96f-4628-815b-32914b8502d3">


# pymytest

`pymytest` is a Python package that allows you to test APIs from the command line. It returns the API response status code, body, and the time taken for execution.

## Installation

You can install the package using pip:

```bash
pip install pymytest
```

## Usage

After installation, you can use the pymytest command followed by the URL of the API you want to test. For example: (add your own api)

```bash 
pymytest GET https://jsonplaceholder.typicode.com/posts/1

pymytest POST https://jsonplaceholder.typicode.com/posts '{"title": "pymytest", "body": "now", "userId": 1}'

pymytest PUT https://jsonplaceholder.typicode.com/posts/1 '{"title": "nnow", "body": "pymytest", "userId": 1}'

pymytest DELETE https://jsonplaceholder.typicode.com/posts/1
```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request on [GitHub](https://github.com/prasadjivane/pymytest/issues).