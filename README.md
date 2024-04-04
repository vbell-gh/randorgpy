# RandomOrgAPI Python Client

A Python client for the Random.org API, providing an easy-to-use interface for generating random data.
I am not connected in any way to the website, just like what they do.

## Features

- All other functions from the BasicApi: <https://api.random.org/json-rpc/4/basic>
  - generateIntegers
  - generateIntegerSequences
  - generateDecimalFractions
  - generateGaussians
  - generateStrings
  - generateUUIDs
  - generateBlobs
  - getUsage
  All these functions are implemented with camel_case

No specific requirements

Example:

```python
from randorgpy import BasicApi

# Create an instance 
api = BasicApi("your-api-key")

# Generate a list of 5 random int between 1 and 10
print(api.generate_integers(5, 1, 10))
