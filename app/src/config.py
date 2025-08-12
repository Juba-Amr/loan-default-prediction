ohe_cols = ['term', 'home_ownership', 'verification_status', 'pymnt_plan',
            'initial_list_status', 'application_type', 'grade']
freq_cols = ['purpose','addr_state']

vars_final = ['delinq_2yrs',
 'last_fico_range_high',
 'last_fico_range_low',
 'acc_now_delinq',
 'open_acc_6m',
 'total_bal_il',
 'il_util',
 'open_rv_12m',
 'all_util',
 'loan_status']

cols_to_keep = ['term', 'emp_length', 'home_ownership', 'annual_inc', 'verification_status','fico_range_low',
                'loan_status', 'pymnt_plan', 'purpose', 'addr_state', 'dti','int_rate', 'fico_range_high',
                'delinq_2yrs', 'earliest_cr_line', 'inq_last_6mths', 'revol_bal', 'initial_list_status',
                'application_type', 'acc_now_delinq', 'tot_coll_amt', 'bc_open_to_buy', 'mo_sin_rcnt_rev_tl_op', 
                'mo_sin_rcnt_tl', 'mort_acc', 'mths_since_recent_bc', 'mths_since_recent_inq', 'num_accts_ever_120_pd', 
                'num_il_tl', 'total_il_high_credit_limit', 'installment', 'grade', 'acc_open_past_24mths', 'avg_cur_bal', 
                'mo_sin_old_rev_tl_op', 'num_actv_rev_tl', 'percent_bc_gt_75', 'pub_rec_bankruptcies', 'tax_liens', 'pub_rec', 
                'revol_util', 'tot_cur_bal', 'num_bc_sats', 'num_bc_tl'
]

#next ones not used anymore
features_to_keep = [
    # Basic loan characteristics
    'loan_amnt', 'funded_amnt', 'term', 'int_rate', 'installment', 
    'grade', 'sub_grade', 'purpose',
    
    # Borrower demographics & employment
    'emp_length', 'home_ownership', 'annual_inc', 'verification_status',
    'zip_code', 'addr_state',
    
    # Financial health indicators
    'dti', 'annual_inc', 'revol_bal', 'revol_util',
    
    # Credit history (core features)
    'fico_range_low', 'fico_range_high', 'earliest_cr_line',
    'delinq_2yrs', 'inq_last_6mths', 'open_acc', 'pub_rec', 'total_acc',
    'mths_since_last_delinq', 'mths_since_last_record',
    
    # Advanced credit metrics (if available at origination)
    'acc_now_delinq', 'tot_coll_amt', 'tot_cur_bal', 'all_util', 
    'total_rev_hi_lim', 'inq_fi', 'total_cu_tl', 'inq_last_12m',
    'acc_open_past_24mths', 'avg_cur_bal', 'bc_open_to_buy', 'bc_util',
    'mort_acc', 'num_accts_ever_120_pd', 'num_actv_bc_tl', 'num_actv_rev_tl',
    'num_bc_sats', 'num_bc_tl', 'num_il_tl', 'num_op_rev_tl', 'num_rev_accts',
    'num_rev_tl_bal_gt_0', 'num_sats', 'pct_tl_nvr_dlq', 'percent_bc_gt_75',
    'pub_rec_bankruptcies', 'tax_liens', 'tot_hi_cred_lim', 'total_bal_ex_mort',
    'total_bc_limit', 'total_il_high_credit_limit',
    
    # Joint application features (if applicable)
    'application_type', 'annual_inc_joint', 'dti_joint', 'verification_status_joint',
    'revol_bal_joint',
    
    # Recent credit behavior
    'open_acc_6m', 'open_act_il', 'open_il_12m', 'open_il_24m',
    'mths_since_rcnt_il', 'total_bal_il', 'il_util', 'open_rv_12m',
    'open_rv_24m', 'max_bal_bc'
]

# Features to DROP - Data leakage, post-origination, or low value
cols_to_drop = [
    # Identifiers (no predictive value)
    'member_id', 'url', 'policy_code',
    
    # Target variable and related (data leakage)
    'loan_status', 'pymnt_plan',
    
    # Post-loan information (data leakage - not available at prediction time)
    'funded_amnt_inv', 'out_prncp', 'out_prncp_inv', 'total_pymnt',
    'total_pymnt_inv', 'total_rec_prncp', 'total_rec_int', 'total_rec_late_fee',
    'recoveries', 'collection_recovery_fee', 'last_pymnt_d', 'last_pymnt_amnt',
    'next_pymnt_d', 'last_credit_pull_d', 'last_fico_range_high', 'last_fico_range_low',
    
    # Post-origination events (data leakage)
    'collections_12_mths_ex_med', 'mths_since_last_major_derog',
    'chargeoff_within_12_mths', 'delinq_amnt', 'mo_sin_old_il_acct',
    'mo_sin_old_rev_tl_op', 'mo_sin_rcnt_rev_tl_op', 'mo_sin_rcnt_tl',
    'mths_since_recent_bc', 'mths_since_recent_bc_dlq', 'mths_since_recent_inq',
    'mths_since_recent_revol_delinq', 'num_tl_120dpd_2m', 'num_tl_30dpd',
    'num_tl_90g_dpd_24m', 'num_tl_op_past_12m',
    
    # Dates (better to engineer features from these)
    'issue_d'
    
    # Employment title (too granular, high cardinality)
    'emp_title',
    
    # Initial list status (internal LendingClub feature)
    'initial_list_status',
    
    # Secondary applicant info (sparse, only for joint applications)
    'sec_app_fico_range_low', 'sec_app_fico_range_high', 'sec_app_earliest_cr_line',
    'sec_app_inq_last_6mths', 'sec_app_mort_acc', 'sec_app_open_acc',
    'sec_app_revol_util', 'sec_app_open_act_il', 'sec_app_num_rev_accts',
    'sec_app_chargeoff_within_12_mths', 'sec_app_collections_12_mths_ex_med',
    'sec_app_mths_since_last_major_derog',
    
    # Hardship and settlement info (post-origination events)
    'hardship_flag', 'hardship_type', 'hardship_reason', 'hardship_status',
    'deferral_term', 'hardship_amount', 'hardship_start_date', 'hardship_end_date',
    'payment_plan_start_date', 'hardship_length', 'hardship_dpd',
    'hardship_loan_status', 'orig_projected_additional_accrued_interest',
    'hardship_payoff_balance_amount', 'hardship_last_payment_amount',
    
    # Settlement info (post-default events)
    'debt_settlement_flag', 'debt_settlement_flag_date', 'settlement_status',
    'settlement_date', 'settlement_amount', 'settlement_percentage', 'settlement_term',
    
    # Disbursement method (operational, not predictive)
    'disbursement_method'
]

print(len(cols_to_drop))