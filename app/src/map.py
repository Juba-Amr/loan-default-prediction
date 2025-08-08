def data_mapping(data):
    mapping = {
        'Fully Paid': 0,
        'Current': 0,
        'In Grace Period': 1,
        'Late (16-30 days)': 2,
        'Late (31-120 days)': 3,
        'Does not meet the credit policy. Status:Fully Paid': 0,
        'Does not meet the credit policy. Status:Charged Off': 4,
        'Charged Off': 4,
        'Default': 5
    }

    data['risk_score']= data['loan_status'].map(mapping)
    data = (data.dropna(subset=['risk_score'])
            .drop(labels='loan_status', axis=1)
            )
    
    data = data.copy()
    print("===> data_mapping called")
    return data