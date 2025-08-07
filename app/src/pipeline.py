from src.config import ohe_cols, freq_cols, cols_to_drop
from src.map import data_mapping
from src.preprocess import filter_matrix, num_data_prep, drop_useless, emp_lenght_map, earliest_to_date, freq_encoding
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer, make_column_selector
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import numpy as np

def pipeline(model, ver=True):
    preprocessor = ColumnTransformer([

        ('scale', RobustScaler(), make_column_selector(dtype_include='number')),
        ('frequency_cols', FunctionTransformer(freq_encoding), freq_cols),
        ('employement_lenght', FunctionTransformer(emp_lenght_map), ['emp_length']),
        ('account_age', FunctionTransformer(earliest_to_date), ['earliest_cr_line']),
        ('cat_left', OneHotEncoder(), ohe_cols)
        
    ], verbose=ver)

    pipe = Pipeline([
        ('features', preprocessor),
        ('model', model)
    ], verbose=ver)

    return pipe

