import pandas as pd

def handle_missing_values(df, method='drop', impute_value=None):
    """
    Handles missing values in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    method (str): 'drop' to drop missing values, 'impute' to fill missing values
    impute_value (optional): Value to replace missing values if method is 'impute'
    
    Returns:
    pd.DataFrame: DataFrame with handled missing values
    """
    # Display missing columns
    missing_cols = df.columns[df.isnull().any()]
    print(f"Columns with missing values: {missing_cols.tolist()}")
    print(f"Missing value counts:\n{df[missing_cols].isnull().sum()}\n")
    
    # Handle missing values
    if method == 'drop':
        df_cleaned = df.dropna()
    elif method == 'impute' and impute_value is not None:
        df_cleaned = df.fillna(impute_value)
    else:
        raise ValueError("Invalid method or impute_value not provided.")
    
    return df_cleaned
