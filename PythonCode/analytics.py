import pandas as pd
import sqlitepac

def get_df():
    rows = sqlitepac.show_all()
    rows = [r for r in rows if len(r) == 8]
    df = pd.DataFrame(rows, columns=['name', 'age', 'illness', 'bill', 'date', 'status', 'height', 'weight'])
    df['date'] = pd.to_datetime(df['date'])
    return df

def get_maxbill():
    df = get_df()
    max_bill = df[df['bill'] == df['bill'].max()]
    return max_bill

def get_oldest():
    df = get_df()
    return df[df['age'] == df['age'].max()]

def get_youngest():
    df = get_df()
    return df[df['age'] == df['age'].min()]

def get_outhospital():
    df = get_df()
    return df[df['status'].str.lower() == 'discharged']
