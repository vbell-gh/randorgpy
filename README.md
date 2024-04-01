# RandomOrgAPI Python Client

A Python client for the Random.org API, providing an easy-to-use interface for generating random data.
I am not connected in any way to the website, just like what they do.

## Features

- Generate random integers, decimal fractions, gaussian numbers, strings, UUIDs, and blobs.
- Generate sequences of random integers.
- All other functions from the BasicApi: <https://api.random.org/json-rpc/4/basic>
- Get usage statistics for the Random.org API.

No specific requirements

Example:

```python
from randord import RandomOrgAPI

# Create an instance 
api = RandomOrgAPI("your-api-key")

# Generate a list of 5 random int between 1 and 10
print(api.generate_integers(5, 1, 10))
