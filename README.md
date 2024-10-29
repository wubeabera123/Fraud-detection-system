Fraud Detection System for E-Commerce and Bank Transactions
Overview
This project focuses on building robust machine learning models to detect fraudulent activities in e-commerce and bank transactions for Adey Innovations Inc. By using advanced data analysis, feature engineering, and machine learning techniques, this system enhances fraud detection, helping prevent financial losses and building trust with customers and financial institutions.

Table of Contents
Overview
Project Structure
Getting Started
Data Description
Tasks and Methodology
1. Data Analysis and Preprocessing
2. Model Building and Training
3. Model Explainability
4. Model Deployment and API Development
5. Dashboard Development
Technologies Used
Results
References
Project Structure
plaintext
Copy code
├── data/
│   ├── Fraud_Data.csv              # E-commerce transaction data
│   ├── IpAddress_to_Country.csv    # Maps IP addresses to countries
│   └── creditcard.csv              # Bank transaction data for credit cards
├── notebooks/
│   ├── data_analysis.ipynb         # Data analysis and feature engineering steps
│   └── model_training.ipynb        # Model training and evaluation
├── src/
│   ├── preprocessing.py            # Data preprocessing functions
│   ├── feature_engineering.py      # Functions for feature creation
│   ├── model_training.py           # Model training scripts
│   ├── explainability.py           # Model explainability scripts (SHAP, LIME)
│   ├── serve_model.py              # Flask app for serving models
│   └── dashboard.py                # Dash dashboard for visualizing insights
├── Dockerfile                      # Docker configuration file
├── requirements.txt                # Python package dependencies
└── README.md                       # Project README file
Getting Started
Clone the repository:

bash
Copy code
git clone <repository-url>
cd fraud-detection-system
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run Data Preprocessing: Execute the data preprocessing steps to clean and transform the data:

bash
Copy code
python src/preprocessing.py
Train the Models:

bash
Copy code
python src/model_training.py
Run the Flask API: Start the API service:

bash
Copy code
python src/serve_model.py
Run the Docker container:

bash
Copy code
docker build -t fraud-detection-model .
docker run -p 5000:5000 fraud-detection-model
Data Description
Fraud_Data.csv: E-commerce transaction data with fields including user_id, signup_time, purchase_time, purchase_value, device_id, source, browser, sex, age, ip_address, and class (target variable for fraud).
IpAddress_to_Country.csv: Contains mappings of IP address ranges to countries.
creditcard.csv: Bank transaction data with fields like Time, anonymized V1 to V28 features, Amount, and Class (target variable for fraud).
Tasks and Methodology
1. Data Analysis and Preprocessing
Handle Missing Values: Impute or drop missing values where appropriate.
Data Cleaning: Remove duplicates, correct data types.
EDA: Perform univariate and bivariate analyses.
Geolocation Analysis: Convert IP addresses to countries.
Feature Engineering: Create transaction frequency, time-based features (hour, day, etc.), and normalize/scale data.
Encoding Categorical Features: Convert categorical data to numerical values for model training.
2. Model Building and Training
Model Selection: We use various models (Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, MLP, CNN, RNN, LSTM) for fraud detection.
Train-Test Split: Split the data into training and testing sets.
Model Training and Evaluation: Train and evaluate models on both datasets, comparing their performance.
3. Model Explainability
SHAP (Shapley Additive Explanations): Used for understanding the contribution of each feature to model predictions, with summary, force, and dependence plots.
LIME (Local Interpretable Model-Agnostic Explanations): Provides local interpretability for individual predictions, offering feature importance insights.
4. Model Deployment and API Development
Flask API: Serve the model as a REST API with endpoints for fraud predictions.
Docker: Containerize the Flask application to ensure consistent deployment across environments.
Logging: Implement Flask-Logging to monitor incoming requests, errors, and fraud predictions.
5. Dashboard Development
Flask & Dash: Create a dashboard using Dash for visualizing insights on fraud cases, transaction trends, and geolocation data.
Interactive Insights: The dashboard includes summaries, fraud trends over time, geographic distribution, device/browser comparison, and transaction data overviews.
Technologies Used
Programming Languages: Python
Libraries: Pandas, NumPy, Scikit-Learn, SHAP, LIME, Flask, Dash, Docker
Machine Learning Models: Logistic Regression, Decision Tree, Random Forest, Gradient Boosting, MLP, CNN, RNN, LSTM
APIs & Containerization: Flask, Docker
Results
This project produces a fraud detection model with enhanced accuracy, using both e-commerce and credit card transaction data. We achieved interpretability using SHAP and LIME for model explainability, and the interactive dashboard offers a comprehensive view of fraud insights.