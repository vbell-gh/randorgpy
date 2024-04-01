import requests
from typing import Union, List


class RandomOrgAPI:
    """
    A class that provides an interface to the Random.org API for generating random data.

    Args:
        api_key (str): The API key for accessing the Random.org API.
        end_point (str, optional): The endpoint URL for the API.
            Defaults to "https://api.random.org/json-rpc/4/invoke".
        timeout (int, optional): The timeout value for the API requests in seconds. Defaults to 10.
        return_metadata (bool, optional): Whether to return metadata in the API responses.
            Defaults to False.
        id (int, optional): The ID to be used in the API requests.
            Defaults to 42.
        The docstring are with the help AI cause I was lazy to write them myself and I pay 10 USD per month for that.
    """

    def __init__(
        self,
        api_key,
        end_point="https://api.random.org/json-rpc/4/invoke",
        timeout=10,
        return_metadata=False,
        id=42,
    ):
        self.api_key = api_key
        self.end_point = end_point
        self.timeout = timeout
        self.return_metadata = return_metadata
        self.id = id

    def send_request(self, method: str, params: dict):
        """
        Sends a request to the OpenApi endpoint using the given method and parameters.

        Args:
            method (str): The method to be called.
            params (dict): The parameters to be passed with the method.

        Returns:
            dict or None: The response from the server as a dictionary, or None if an error occurred.

        Raises:
            requests.exceptions.Timeout: If the request times out.
            requests.exceptions.RequestException: If there is an error with the request.
            Exception: If an unexpected error occurs.
        """
        payload = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
            "id": self.id,
        }
        try:
            response = requests.post(self.end_point, json=payload, timeout=self.timeout)
        except requests.exceptions.Timeout as e:
            print(f"The request timed out: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"There was an error with the request: {e}")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        if self.return_metadata:
            return response.json()
        else:
            if method == "getUsage":
                return response.json()["result"]
            else:
                return response.json()["result"]["random"]["data"]

    def generate_integers(
        self, n: int, minimum: int, maximum: int, replacement=True, base=10
    ):
        """generate_integers generates true random integers within a defined range.

        Args:
            n (int): Number of integers to generate.
            minimum (int): Maximum value of the integers.
            maximum (int): Minimum value of the integers.
            replacement (bool, optional): Should replacements be allowed. Defaults to True.
            base (int, optional): Base of the integers generated. Defaults to 10.

        Returns:
            Random integers within the defined range.
        """
        parameters = {
            "apiKey": self.api_key,
            "n": n,
            "min": minimum,
            "max": maximum,
            "replacement": replacement,
            "base": base,
        }

        return self.send_request("generateIntegers", parameters)

    def generate_integer_sequence(
        self,
        n: int,
        length: Union[int, List[int]],
        minimum: Union[int, List[int]],
        maximum: Union[int, List[int]],
        replacement: Union[bool, List[bool]],
        base: Union[int, List[int]],
    ):
        """generate_integer_sequence generates integer sequences.

        Args:
            n (int): The number of sequences to generate.
            length (Union[int, List[int]]): The length of each sequence.
                It can be a single integer or a list of integers.
            minimum (Union[int, List[int]]): The minimum value for each element in the sequence.
                It can be a single integer or a list of integers.
            maximum (Union[int, List[int]]): The maximum value for each element in the sequence.
                It can be a single integer or a list of integers.
            replacement (Union[bool, List[bool]]): A boolean value or a list of boolean values
                indicating whether the elements in the sequence should be generated with replacement
                (True) or without replacement (False).
            base (Union[int, List[int]]): The base for the generated sequences.
                It can be a single integer or a list of integers.

        Returns:
            An integer sequences.

        """
        parameters = {
            "apiKey": self.api_key,
            "n": n,
            "length": length,
            "min": minimum,
            "max": maximum,
            "replacement": replacement,
            "base": base,
        }

        return self.send_request("generateIntegerSequences", parameters)

    def generate_decimal_fractions(self, n: int, decimal_places: int, replacement=True):
        """
        Generates a list of random decimal fractions.

        Args:
            n (int): The number of decimal fractions to generate.
            decimalPlaces (int): The number of decimal places for each fraction.
            replacement (bool, optional): Specifies whether to allow duplicate fractions.
                Defaults to True.

        Returns:
            list: A list of randomly generated decimal fractions.

        """
        parameters = {
            "apiKey": self.api_key,
            "n": n,
            "decimalPlaces": decimal_places,
            "replacement": replacement,
        }

        return self.send_request("generateDecimalFractions", parameters)

    def generate_gaussian(
        self, n: int, mean: float, std: float, significant_digits: int
    ):
        """
        Generates a list of random numbers following a Gaussian distribution.

        Args:
            n (int): The number of random numbers to generate.
            mean (float): The mean of the Gaussian distribution.
            std (float): The standard deviation of the Gaussian distribution.
            significant_digits (int): The number of significant digits
                to round the generated numbers to.

        Returns:
            A list of random numbers following a Gaussian distribution.

        """
        parameters = {
            "apiKey": self.api_key,
            "n": n,
            "mean": mean,
            "stdDev": std,
            "significantDigits": significant_digits,
        }
        return self.send_request("generateGaussians", parameters)

    def generate_strings(self, n: int, length: int, characters: str, replacement=True):
        """
        Generates random strings.

        Args:
            n (int): The number of strings to generate.
            length (int): The length of each generated string.
            characters (str): The characters to use for generating the strings.
            replacement (bool, optional): Whether to allow replacement of characters.
                Defaults to True.

        Returns:
            Randomly generated strings.
        """
        parameters = {
            "apiKey": self.api_key,
            "n": n,
            "length": length,
            "characters": characters,
            "replacement": replacement,
        }
        return self.send_request("generateStrings", parameters)

    def generate_uuids(self, n: int):
        """
        Generates a list of UUIDs.

        Args:
            n (int): The number of UUIDs to generate.

        Returns:
            list: A list of generated UUIDs.
        """
        parameters = {"apiKey": self.api_key, "n": n}
        return self.send_request("generateUUIDs", parameters)

    def generate_blobs(self, n: int, size: int, fmt="base64"):
        """
        Generates random blobs.

        Args:
            n (int): The number of blobs to generate.
            size (int): The size of each blob in bytes.
            fmt (str, optional): The format of the generated blobs. Defaults to "base64".

        Returns:
            The generated blobs.
        """
        parameters = {"apiKey": self.api_key, "n": n, "size": size, "format": fmt}
        return self.send_request("generateBlobs", parameters)

    def get_usage(self):
        """
        Retrieves the usage statistics for the random.org API.

        Returns:
            dict: A dictionary containing the usage statistics.
        """
        parameters = {"apiKey": self.api_key}
        return self.send_request("getUsage", parameters)


if __name__ == "__main__":
    pass
