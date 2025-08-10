def data_mapping(data):
    mapping = {
        'Fully Paid': 0,
        'Current': 0,
        'In Grace Period': 1,
        'Late (16-30 days)': 1,
        'Late (31-120 days)': 1,
        'Does not meet the credit policy. Status:Fully Paid': None,
        'Does not meet the credit policy. Status:Charged Off': None,
        'Charged Off': 1,
        'Default': 1
    }

    data['loan_status']= data['loan_status'].map(mapping)
    data = data.dropna(subset=['loan_status'])
            
    print("===> data_mapping called")
    return data
    
