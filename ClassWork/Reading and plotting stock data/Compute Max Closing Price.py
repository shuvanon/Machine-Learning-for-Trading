import pandas as pd

def get_max_close(symbol):

    df =pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()

def get_min_volume(symbol):

    df =pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].min()

def test_run():

    for symbol in ['AAPL', 'IBM']:
        print("MAX Close")
        print(symbol, get_max_close(symbol))
        print("Min Volume")
        print(symbol, get_min_volume(symbol))


if __name__ == "__main__":
    test_run()