from flask import Flask, request, jsonify
import joblib
import numpy as np
import logging
from logging import FileHandler, Formatter
from tensorflow.keras.models import load_model

# Initialize Flask app
app = Flask(__name__)

# Configure logging
handler = FileHandler('app.log')  # Log to app.log file
handler.setFormatter(Formatter('%(asctime)s - %(levelname)s - %(message)s'))
app.logger.addHandler(handler)
app.logger.setLevel(logging.INFO)

# Load models
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
    app.logger.info('Received data: %s', data)

    # Ensure the input data is valid
    if not data or 'input_data' not in data:
        app.logger.error('No input data provided')
        return jsonify({'error': 'No input data provided'}), 400

    # Check that input_data is a list or array
    input_data = data['input_data']
    if not isinstance(input_data, list) or len(input_data) == 0:
        app.logger.error('Input data must be a non-empty list')
        return jsonify({'error': 'Input data must be a non-empty list'}), 400

    # Reshape input data for the model
    try:
        input_array = np.array(input_data).reshape(1, -1)
    except Exception as e:
        app.logger.error('Invalid input data format: %s', str(e))
        return jsonify({'error': f'Invalid input data format: {str(e)}'}), 400

    # Make predictions using the model
    try:
        rf_prediction = rf_model.predict(input_array)[0]
        app.logger.info('Random Forest prediction: %d', int(rf_prediction))
        response = {
            'RandomForest': int(rf_prediction)
        }
        return jsonify(response), 200

    except Exception as e:
        app.logger.error('Prediction failed: %s', str(e))
        return jsonify({'error': f'Prediction failed: {str(e)}'}), 500

# Run the app normally
if __name__ == '__main__':
    app.run(debug=True)
