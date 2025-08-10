import pandas as pd
import sklearn
from imblearn.combine import SMOTETomek
from src.config import freq_cols

def balance_dataframe(df: pd.DataFrame, df_y: pd.Series, pipe: sklearn.pipeline):

    df_copy = df.copy()

    df_copy = pipe['features'].fit_transform(df)
    smote_tomek = SMOTETomek(random_state=42)
    X_resampled, y_resampled = smote_tomek.fit_resample(df_copy, df_y)

    #because SMOTEtomek converts to numpy array we cast back to pandas DataFrame
    num_cols = [col for col in df.columns if df[col].dtype != 'object']
    feature_names = num_cols + freq_cols + ['emp_lenght', 'earliest_cr_line'] + list(pipe[0]['OHE'].get_feature_names_out())

    df_resampled = pd.DataFrame(X_resampled, columns=feature_names)
    df_y_resampled = pd.DataFrame(y_resampled, columns='loan_status')
    

    return df_resampled, df_y_resampled