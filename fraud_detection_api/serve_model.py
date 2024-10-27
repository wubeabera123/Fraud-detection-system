from flask import Flask, request, jsonify
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the Random Forest model
rf_model = joblib.load('../saved_models/random_forest_fraud_model.pkl')

# Define a basic root route
@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Fraud Detection API is running."}), 200

# Define route for model prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()
    print('data ....', data)
    
    # Ensure the input data is valid
    if not data or 'input_data' not in data:
        return jsonify({'error': 'No input data provided'}), 400

    # Check that input_data is a list or array and has exactly 13 features
    input_data = data['input_data']
    if not isinstance(input_data, list) or len(input_data) != 13:  # Expecting 13 features
        return jsonify({'error': 'Input data must be a list of 13 features'}), 400

    # Reshape input data for the Random Forest model
    try:
        input_array = np.array(input_data).reshape(1, -1)
    except Exception as e:
        return jsonify({'error': f'Invalid input data format: {str(e)}'}), 400

    # Make predictions using the Random Forest model
    try:
        rf_prediction = rf_model.predict(input_array)[0]

        # Prepare the response dictionary
        response = {
            'RandomForest': int(rf_prediction)
        }
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

# Run the app normally
if __name__ == '__main__':
    app.run(debug=True)
