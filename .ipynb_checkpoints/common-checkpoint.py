import pandas as pd
def load_data(filename):
    df = pd.read_csv(filename)
    df = df.rename(columns={"foo": "bar"})
    return df

