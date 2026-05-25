import pandas as pd
import sqlitepac

def get_df():
    rows = sqlitepac.show_all()
    rows = [r for r in rows if len(r) == 8]
    df = pd.DataFrame(rows, columns=['name', 'age', 'illness', 'bill', 'date', 'status', 'height', 'weight'])
    df['status'] = df['status'].str.lower()
    df['date'] = pd.to_datetime(df['date']).dt.date
    return df

def status_bills():
    df = get_df()
    return df.groupby('status')['bill'].sum().reset_index()

def admitted_per_day():
    df = get_df()
    return df[df['status'] == 'admitted'].groupby('date').size().reset_index(name='count')

def discharged_per_day():
    df = get_df()
    return df[df['status'] == 'discharged'].groupby('date').size().reset_index(name='count')

def daily_total_bills():
    df = get_df()
    return df.groupby('date')['bill'].sum().reset_index()

def daily_avg_bills():
    df = get_df()
    return df.groupby('date')['bill'].mean().reset_index()

def count_by_illness():
    df = get_df()
    return df.groupby('illness').size().reset_index(name='count')
