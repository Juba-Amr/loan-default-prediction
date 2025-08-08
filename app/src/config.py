ohe_cols = ['term','debt_settlement_flag','initial_list_status','verification_status','home_ownership']
freq_cols = ['purpose','addr_state']

"""
cols_to_drop=['sub_grade','issue_d','url','emp_title','settlement_date','verification_status_joint',
                'sec_app_earliest_cr_line','zip_code','pymnt_plan','application_type','disbursement_method',
                'debt_settlement_flag_date','settlement_status','hardship_start_date','hardship_end_date',
                'payment_plan_start_date','next_pymnt_d','issue_d','grade','hardship_type','last_pymnt_d',
                'last_credit_pull_d','hardship_loan_status','hardship_flag','hardship_status','hardship_reason',
                'out_prncp', 'total_pymnt', 'last_pymnt_amnt', 'total_rec_int', 'total_rec_late_fee','recoveries',
                'int_rate', 'chargeoff_within_12_mths', 'delinq_amnt', 'acc_now_delinq','debt_settlement_flag_Y',
                'debt_settlement_flag_N','last_fico_range_low','last_fico_range_high','total_rec_prncp',
                'out_prncp_inv ','collection_recovery_fee','total_pymnt_inv '
                ]
"""   
             
cols_to_drop = [
    # Pure ID / metadata / text not useful for prediction
    'url', 'emp_title', 'zip_code', 'pymnt_plan',
    'application_type', 'disbursement_method',

    # Dates after loan issuance (leakage)
    'issue_d', 'settlement_date', 'debt_settlement_flag_date',
    'hardship_start_date', 'hardship_end_date', 'payment_plan_start_date',
    'next_pymnt_d', 'last_pymnt_d', 'last_credit_pull_d',

    # Outcome variables or directly derived from outcome (leakage)
    'out_prncp', 'total_pymnt', 'last_pymnt_amnt', 'total_rec_int',
    'total_rec_late_fee', 'recoveries', 'total_rec_prncp',
    'out_prncp_inv ', 'collection_recovery_fee', 'total_pymnt_inv ',

    # Flags/status that reflect post-loan events (leakage)
    'settlement_status', 'hardship_type', 'hardship_loan_status',
    'hardship_flag', 'hardship_status', 'hardship_reason',

    # Variables giving away default/payment info
    'chargeoff_within_12_mths', 'delinq_amnt', 'acc_now_delinq',

    # Redundant with target leakage flags
    'debt_settlement_flag_Y', 'debt_settlement_flag_N',

    # FICO scores taken after loan issuance (leakage)
    'last_fico_range_low', 'last_fico_range_high',

    # Redundant with each other (grade/sub_grade)
    'sub_grade',

    # Joint applicant post-issue data
    'verification_status_joint', 'sec_app_earliest_cr_line',

    # Interest rate, if it's the agreed rate, it’s assigned at issuance and may encode outcome
    'int_rate'
]

print(len(cols_to_drop))