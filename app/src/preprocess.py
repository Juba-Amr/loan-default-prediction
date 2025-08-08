import pandas as pd
import numpy as np
from src.config import cols_to_drop
from src.map import data_mapping

class BeforePipeline:
    def __init__(self):
        pass

    def filter_matrix(self, corr_matrix):
        coef_dict = {}
        #we'll get correlated columns in a dict 
        for i,col1 in enumerate(corr_matrix.columns):
            for j,col2 in enumerate(corr_matrix.columns):
                if j<i: #we do this to go throught only the triangular half so we filter the diagonal and avoid dupes (a,b)(b,a) 
                    correlation = corr_matrix.loc[col1,col2]
                    if np.abs(correlation) >= 0.9:
                        coef_dict[(col1,col2)] = correlation
        return coef_dict

    def num_data_prep(self, data):
        """
        #removed this algorithm because it used to take out some columns that were signal so features cleaning will be done manually


        num_cols = [col for col in data.columns if data[col].dtype != 'object']
        data[num_cols] = data[num_cols].replace([np.inf, -np.inf], np.nan) #we clear infinites

        mat = data[num_cols].corr()

        coef_dict= self.filter_matrix(mat)
        temp_set = set()
        for a,b in coef_dict.keys():
            if a not in temp_set:
                temp_set.add(a)
                data = data.drop(labels=a, axis=1)
        """     

        cols_over_30pct_nan = data.columns[data.isna().mean() > 0.3].tolist()
        data = data.drop(labels=cols_over_30pct_nan, axis=1)

        num_cols = [col for col in data.columns if data[col].dtype != 'object']
        data[num_cols] = data[num_cols].fillna(data[num_cols].median())

        print("===> num_data_prep called")
        return data

    def drop_useless(self, data):
        print(f'number of cols to drop: {len(cols_to_drop)}')
        print(f'data shape before dropping: {data.shape}')

        data = data.drop(labels=cols_to_drop, axis=1)
        
        print(f'{len(cols_to_drop)} columns dropped successfuly')
        print(f'data shape after dropping: {data.shape}')

        print("===> drop_useless called")
        return data

    def clean_infinite_and_nan(self, df):
        num_cols = [col for col in df.columns if df[col].dtype != 'object']

        df[num_cols] = df[num_cols].replace([np.inf, -np.inf], np.nan)
        df[num_cols] = df[num_cols].fillna(df[num_cols].median()) 
        print("===> clean infinites called")
        return df
        
    def all_before_pipeline(self, data):
        data = self.clean_infinite_and_nan(data)

        data = data_mapping(data)
        
        data = self.num_data_prep(data)
        
        data = self.drop_useless(data)
        
        data = self.clean_infinite_and_nan(data)
        
        return data

class PreprocessorCustomFunctions:
    def __init__(self):
        pass

    def freq_encoding(self, categoric_data):
        for col in ['purpose', 'addr_state']:
            freq_encoding = categoric_data[col].value_counts(normalize=True)
            categoric_data[col + '_freq'] = categoric_data[col].map(freq_encoding)

        categoric_data.drop(columns=['purpose', 'addr_state'], inplace=True)
        #print(f'frequency data encoded successfuly')
        return categoric_data
    
    def earliest_to_date(self, categoric_data):

        categoric_data = categoric_data.copy()
        categoric_data['earliest_cr_line'] = pd.to_datetime(
            categoric_data['earliest_cr_line'], format='%b-%Y', errors='coerce'
        )
        #print(f"Rows with invalid 'earliest_cr_line': {categoric_data['earliest_cr_line'].isna().sum()}")

        #took this part out because we'll need all the columns transformers to output the same number of rows, we'll drop them later
        #categoric_data = categoric_data[categoric_data['earliest_cr_line'].notna()] 
        #print(f"Rows with invalid 'earliest_cr_line' after droping: {categoric_data['earliest_cr_line'].isna().sum()}")

        today = pd.to_datetime('today')
        categoric_data['credit_history_length'] = (today - categoric_data['earliest_cr_line']).dt.days

        categoric_data = pd.DataFrame(categoric_data).drop(columns=['earliest_cr_line'], axis=1)

        #print(f"Remaining rows: {len(categoric_data)}, earliest cr data encoded successfuly")
        #print("earliest cr data encoded successfuly")
        return categoric_data
    
    def emp_lenght_map(self, categoric_data):
        map_emp_lenght = {
            None: -1,'< 1 year': 0,'1 year':1,'2 years':2,'3 years':3,
            '4 years':4,'5 years':5,'6 years':6,'7 years':7,'8 years':8,
            '9 years':9,'10+ years':10
        }
        categoric_data['length'] = categoric_data['emp_length'].map(map_emp_lenght)
        categoric_data = categoric_data.drop(labels='emp_length',axis=1)
        #print('employement lenght encoded successfuly')
        return categoric_data

