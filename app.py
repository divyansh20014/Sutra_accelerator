# from flask import Flask, jsonify, request
# import json

# app = Flask(__name__)

# # Define the path to the JSON file containing the combined data
# JSON_FILE_PATH = 'combined_data.json'

# @app.route('/', methods=['GET'])
# def get_combined_data():
#     """
#     API endpoint to get combined transaction and customer profile data from JSON file.
#     """
#     try:
#         # Read the combined data from the JSON file
#         with open(JSON_FILE_PATH, 'r') as json_file:
#             combined_data = json.load(json_file)
        
#         # Return the combined data as JSON response
#         return jsonify(combined_data), 200

#     except FileNotFoundError:
#         return jsonify({"error": "Data file not found"}), 404

#     except json.JSONDecodeError:
#         return jsonify({"error": "Error decoding JSON data"}), 500

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500

# # if __name__ == "__main__":
# #     app.run(host='0.0.0.0', port=5000, debug=True)


# app.py
from flask import Flask, jsonify
import json
from fetch_customer_profile import get_customer_profile

app = Flask(__name__)

# Define the testing transaction data directly in app.py
transaction_data = {
    'custID': 5,
    'transaction_amount': 15000.00,
    'timestamp': '2024-08-23T16:55:07.999868',
    'country': 'North Korea',
    'region': 'Pyongyang',
    'occupation': 'Politician'
}

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

@app.route('/api/combined-data', methods=['GET'])
def get_combined_data():
    """
    API endpoint to get combined transaction and customer profile data.
    """
    try:
        combined_data = combine_transaction_and_profile(transaction_data)
        
        if combined_data:
            return jsonify(combined_data), 200
        else:
            return jsonify({"error": "Failed to combine data"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=4000, debug=True)
