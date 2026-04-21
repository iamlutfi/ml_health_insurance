
def validate_input(df):
    # Check importance column must have
    required_cols = ['bmi', 'smoker', 'bloodpressure', 'age']
    missing_col = [col for col in required_cols if col not in df.columns]
    if missing_col:
        raise ValueError(f'Error: Importance colomn missing {missing_col}')
    
    # Check missing value
    if df.isna().values.any():
        null_cols = df.columns[df.isna().any()].tolist()
        null_rows = [idx + 1 for idx in df[df.isna().any()(axis=1)].index.tolist()]
        return False, f'Missing value found in columns: {null_cols} at row: {null_rows}'
    
    # check logical data limits on important columns
    if (df['age'] <=0).any() or (df['age'] >= 110).any():
        return False, 'Abnormal age value!'
    
    if (df['bmi'] <=0).any():
        return False, 'Abnormal BMI value!' 
    
    if (df['bloodpressure'] <= 0).any() or (df['bloodpressure'] >= 300).any():
        return False, 'Abnormal bloodpressure value!'
    
    return True, 'Valid'