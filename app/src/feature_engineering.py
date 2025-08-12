import pandas as pd
import numpy as np

def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds high-value engineered features from dataset
    """
    df = df.copy()
    
    df['revol_bal_to_income'] = df['revol_bal'] / (df['annual_inc'] + 1)
    df['installment_to_income'] = df['installment'] / (df['annual_inc'] + 1)
    df['total_il_limit_to_income'] = df['total_il_high_credit_limit'] / (df['annual_inc'] + 1)
    df['revol_bal_ratio'] = df['revol_bal'] / (df['bc_open_to_buy'] + df['revol_bal'] + 1)

    df['avg_old_rev_age'] = df['mo_sin_old_rev_tl_op'] / (df['num_actv_rev_tl'] + 1)
    df['avg_recent_installment_age'] = df['mo_sin_rcnt_tl'] / (df['num_il_tl'] + 1)
    df['avg_recent_bc_age'] = df['mths_since_recent_bc'] / (df['num_bc_tl'] + 1)
    

    df['delinq_flag'] = (df['delinq_2yrs'] > 0).astype(int)
    df['public_record_flag'] = ((df['pub_rec_bankruptcies'] > 0) | 
                                (df['tax_liens'] > 0) | 
                                (df['pub_rec'] > 0)).astype(int)
    df['serious_delinquency_flag'] = (df['num_accts_ever_120_pd'] > 0).astype(int)

    grade_map = {g: i for i, g in enumerate(sorted(df['grade'].unique()), start=1)}
    df['grade_num'] = df['grade'].map(grade_map)
    df['grade_int_rate'] = df['grade_num'] * df['int_rate']

    df['total_credit_balance'] = df['revol_bal'] + df['avg_cur_bal'] + df['tot_cur_bal']
    df['avg_balance_per_account'] = df['tot_cur_bal'] / (df['num_bc_sats'] + 1)

    return df