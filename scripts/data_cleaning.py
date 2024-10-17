def clean_data(df, dtype_mappings=None):
    """
    Cleans data by removing duplicates and correcting data types.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame
    dtype_mappings (dict): Dictionary with column names as keys and data types as values
    
    Returns:
    pd.DataFrame: Cleaned DataFrame
    """
    # Remove duplicates
    initial_shape = df.shape
    df_cleaned = df.drop_duplicates()
    print(f"Removed {initial_shape[0] - df_cleaned.shape[0]} duplicate rows.")
    
    # Correct data types if dtype_mappings is provided
    if dtype_mappings:
        for col, dtype in dtype_mappings.items():
            try:
                df_cleaned[col] = df_cleaned[col].astype(dtype)
                print(f"Converted column '{col}' to {dtype}.")
            except ValueError as e:
                print(f"Error converting column '{col}' to {dtype}: {e}")
    
    return df_cleaned
