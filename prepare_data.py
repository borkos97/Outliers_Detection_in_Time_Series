import pandas as pd

def prepare_data(dataset):
    df = pd.read_csv(dataset, header=0)
    keep_col = ['Date', 'MaxTemp']
    new_df = df[keep_col]
    new_df = new_df.groupby("Date")["MaxTemp"].sum().rename("temperature")
    new_df.to_csv('file.csv')
    return new_df