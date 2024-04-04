import requests


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
        The docstring are with the help AI cause I was lazy to write them myself and I pay 10 USD per month for that anyway.
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


if __name__ == "__main__":
    pass
