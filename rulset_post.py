
import requests
import json
from datetime import datetime
from Combine_data import combine_transaction_and_profile

# URL of the API endpoint to send the POST request
api_url = "http://sasserver.demo.sas.com/microanalyticScore/modules/Accelerator_RS_11_0/steps/execute"  # Replace with your actual API URL

# Function to send POST request
def send_post_request():
    # Example transaction data (replace with actual data)
    transaction_data = {
        'custID': 1,  # Example customer ID
        'transaction_amount': 15000.00,
        'timestamp': datetime.now().isoformat(),
        'country': 'North Korea',
        'region': 'Pyongyang',
        'occupation': 'Politician'
    }

    customer_id = transaction_data['custID']  # Extract customer ID from transaction data

    # Combine transaction data with customer profile data
    combined_data = combine_transaction_and_profile(transaction_data, customer_id)

    if combined_data:
        # Extract the required fields from the combined data
        def get_value_from_profile(profile, field_name):
            # Iterate over the list to find the matching name field
            for item in profile:
                if item["name"] == field_name:
                    return item["value"]
            return None  # Return None if the field is not found

        # Extract values
        count = get_value_from_profile(combined_data["customer_profile"], "transaction_count_last_20_minutes")
        last_transaction_time = get_value_from_profile(combined_data["customer_profile"], "last_transaction_time")
        new_transaction_timestamp = transaction_data['timestamp']

        # Prepare data for POST request
        post_data = {
            "custID": customer_id,
            "count": count,
            "last_transaction_time": last_transaction_time,
            "new_transaction_timestamp": new_transaction_timestamp
        }

        # Send POST request to the API
        response = requests.post(api_url, json=post_data)

        if response.status_code == 200:
            print("POST request successful.")
            print("Response:", response.json())
        else:
            print(f"Failed to send POST request. Status code: {response.status_code}")
            print("Response:", response.text)
    else:
        print("Failed to combine data.")

if __name__ == "__main__":
    send_post_request()