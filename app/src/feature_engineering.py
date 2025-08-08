import pandas as pd
import numpy as np

def add_engineered_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds engineered credit risk features to dataset.
        Fixed to prevent infinities from division by zero.
    """
    
    def safe_divide(numerator, denominator):
        """Safely divide two series, avoiding infinities"""
        # Replace zeros and negatives in denominator with NaN
        safe_denom = denominator.replace(0, np.nan)
        safe_denom = safe_denom.where(safe_denom > 0, np.nan)  # Also handle negatives
        return numerator / safe_denom

    new_features = pd.DataFrame({
        # Income ratios - protect against zero/negative income
        'loan_to_income': safe_divide(df['loan_amnt'], df['annual_inc']),
        'revol_bal_to_income': safe_divide(df['revol_bal'], df['annual_inc']),
        'tot_cur_bal_to_income': safe_divide(df['tot_cur_bal'], df['annual_inc']),
        'bc_limit_to_income': safe_divide(df['total_bc_limit'], df['annual_inc']),

        # Credit limit ratios
        'total_utilization': safe_divide(df['revol_bal'], df['total_rev_hi_lim']),
        'bc_to_total_limit_ratio': safe_divide(df['total_bc_limit'], df['total_rev_hi_lim']),

        # Account ratios
        'recent_account_ratio': safe_divide(df['acc_open_past_24mths'], df['total_acc']),
        'active_to_total_accounts': safe_divide(df['num_actv_rev_tl'], df['total_acc']),
        'pct_bc_gt_75_ratio': safe_divide(df['percent_bc_gt_75'], df['num_bc_tl']),

        # Risk flags - these should be safe as they're boolean operations
        'high_util_flag': (df['revol_util'] > 80).astype(int),
        'many_inquiries_flag': (df['inq_last_6mths'] >= 3).astype(int)
    }, index=df.index)

    df = pd.concat([df, new_features], axis=1)
    return df

