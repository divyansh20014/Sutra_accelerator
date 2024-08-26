# import json
# from fetch_customer_profile import get_customer_profile

# def format_profile_or_transaction(data_dict):
#     """
#     Transform a dictionary into a list of dictionaries with 'name' and 'value' keys.
    
#     Args:
#     - data_dict (dict): The original dictionary to be transformed.

#     Returns:
#     - list: A list of dictionaries with 'name' and 'value' keys.
#     """
#     return [{"name": key, "value": str(value)} for key, value in data_dict.items()]

# def combine_transaction_and_profile(transaction, customer_id):
#     """
#     Combine transaction data with customer profile data and save to JSON.

#     Args:
#     - transaction (dict): Transaction data.
#     - customer_id (int): Customer ID for fetching profile data.

#     Returns:
#     - dict: Combined data if successful, else None.
#     """
#     profile = get_customer_profile(customer_id)
    
#     if profile:
#         # Transform both the profile and transaction data
#         formatted_profile = format_profile_or_transaction(profile)
#         formatted_transaction = format_profile_or_transaction(transaction)
        
#         combined_data = {
#             "customer_profile": formatted_profile,
#             "transaction": formatted_transaction
#         }
        
#         # Save combined data to JSON file
#         with open('combined_data.json', 'w') as json_file:
#             json.dump(combined_data, json_file, indent=4)
        
#         return combined_data
#     return None

# # Example usage
# if __name__ == "__main__":
#     # Sample transaction data (replace with actual data)
#     transaction_data = {
#         'country': 'North Korea',
#         'custID': 1,
#         'occupation': 'Politician',
#         'region': 'Pyongyang',
#         'timestamp': '2024-08-22T23:13:32.689253',
#         'transaction_amount': 15000.00
#     }
    
#     customer_id = 1  # Replace with actual customer ID
#     combined_data = combine_transaction_and_profile(transaction_data, customer_id)
    
#     if combined_data:
#         print("Combined data saved successfully.")
#     else:
#         print("Failed to combine data.")


from fetch_customer_profile import get_customer_profile

def format_profile_or_transaction(data_dict):
    """
    Transform a dictionary into a list of dictionaries with 'name' and 'value' keys.
    
    Args:
    - data_dict (dict): The original dictionary to be transformed.

    Returns:
    - list: A list of dictionaries with 'name' and 'value' keys.
    """
    return [{"name": key, "value": str(value)} for key, value in data_dict.items()]

def combine_transaction_and_profile(transaction):
    """
    Combine transaction data with customer profile data and return as a dictionary.
    
    Args:
    - transaction (dict): Transaction data.

    Returns:
    - dict: Combined data if successful, else None.
    """
    customer_id = transaction.get('custID')
    profile = get_customer_profile(customer_id)
    
    if profile:
        # Transform both the profile and transaction data
        formatted_profile = format_profile_or_transaction(profile)
        formatted_transaction = format_profile_or_transaction(transaction)
        
        combined_data = {
            "customer_profile": formatted_profile,
            "transaction": formatted_transaction
        }
        
        return combined_data
    return None
