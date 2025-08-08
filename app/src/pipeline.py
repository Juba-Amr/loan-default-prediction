from src.config import ohe_cols, freq_cols
from src.preprocess import PreprocessorCustomFunctions
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector


custom_preprocessor = PreprocessorCustomFunctions()


def pipeline(model, ver=True):
    preprocessor = ColumnTransformer([

        ('scale', RobustScaler(), make_column_selector(dtype_include='number')),
        ('frequency_cols', FunctionTransformer(custom_preprocessor.freq_encoding), freq_cols),
        ('employement_lenght', FunctionTransformer(custom_preprocessor.emp_lenght_map), ['emp_length']),
        ('account_age', FunctionTransformer(custom_preprocessor.earliest_to_date), ['earliest_cr_line']),
        ('OHE', OneHotEncoder(), ohe_cols)
        
    ], verbose=ver)

    pipe = Pipeline([
        ('features', preprocessor),
        ('model', model)
    ], verbose=ver)

    return pipe

