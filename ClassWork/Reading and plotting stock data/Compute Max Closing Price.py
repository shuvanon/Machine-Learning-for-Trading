import pandas as pd

def get_max_close(symbol):

    df =pd.read_csv("data/{}.csv".format(symbol))
    return df['Close'].max()

def get_mean_volume(symbol):

    df =pd.read_csv("data/{}.csv".format(symbol))
    return df['Volume'].mean()

def test_run():

    for symbol in ['AAPL', 'IBM']:
        print("MAX Close")
        print(symbol, get_max_close(symbol))
        print("Mean Volume")
        print(symbol, get_mean_volume(symbol))


if __name__ == "__main__":
    test_run()