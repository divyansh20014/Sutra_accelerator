import requests

def fetch_transaction_from_api(api_url, api_key):
    """
    Fetch transaction details from the given API endpoint using the provided API key.
    
    Args:
    - api_url (str): The URL of the API endpoint to fetch transaction data.
    - api_key (str): The API key for authentication.

    Returns:
    - dict: Transaction data in JSON format if successful, else None.
    """
    headers = {'Authorization': f'Bearer {api_key}'}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        return response.json()  # Assuming the API returns JSON data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    
    return None