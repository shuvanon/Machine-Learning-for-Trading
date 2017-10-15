Import pandas as import pdb; pdb.set_trace()

def test_run():
    df = pd.read_csv("data/AAPL.csv")
    print(df)
    print(df.head())
    print(df.tail())


if __name__ == "__main__":
    test_run()