from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Define the path to the JSON file containing the combined data
JSON_FILE_PATH = 'combined_data.json'

@app.route('/', methods=['GET'])
def get_combined_data():
    """
    API endpoint to get combined transaction and customer profile data from JSON file.
    """
    try:
        # Read the combined data from the JSON file
        with open(JSON_FILE_PATH, 'r') as json_file:
            combined_data = json.load(json_file)
        
        # Return the combined data as JSON response
        return jsonify(combined_data), 200

    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404

    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON data"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000, debug=True)
