import pandas as pd
import numpy as np

def transform(df):
    # copy df to prevent the original data from being transformed
    transform_df = df.copy()
    
    # mapping smoker
    transform_df['smoker'] = transform_df['smoker'].astype(str).str.lower().map({'yes': 1, 'no': 0})
    
    # --- feature engginering ---
    transform_df['smoker_bmi'] = transform_df['smoker'] * transform_df['bmi']
    transform_df['smoker_age'] = transform_df['smoker'] * transform_df['age']
    if all(col in transform_df.columns for col in ['smoker', 'bmi', 'bloodpressure']):
        transform_df['health_risk_score'] = ((transform_df['smoker'] * 3) + 
                                             (transform_df['bmi'] > 30).astype(int) * 2 + 
                                             (transform_df['bloodpressure'] >=  140).astype(int) * 1
                                            )
    
    bins_bp = [0, 119, 139, np.inf]
    labels_bp = ['Normal', 'Pre-Hypertension', 'Hypertension']
    transform_df['bp_status'] = pd.cut(transform_df['bloodpressure'], bins=bins_bp, labels=labels_bp)
    
    mapping_bp = {'Normal':0, 'Pre-Hypertension':1, 'Hypertension':2}
    transform_df['bp_status'] = transform_df['bp_status'].map(mapping_bp)
    
    # final selection
    top_features = ['smoker_bmi', 'smoker', 'smoker_age', 'health_risk_score', 'bloodpressure', 'bp_status'] 
    
    return transform_df[top_features]
