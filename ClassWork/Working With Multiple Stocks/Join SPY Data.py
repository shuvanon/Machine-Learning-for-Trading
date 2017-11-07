import pandas as pd

def test_run():
    #define date range
    start_date='2010-01-22'
    end_date='2010-01-26'
    dates=pd.date_range(start_date,end_date)

    #create an empty dataframe
    df1=pd.DataFrame(index=dates)
    print(df1)

    #Read spy data
    dfSPY = pd.read_csv("data/SPY.csv", index_col="Date", parse_dates=True)
    #print(dfSPY)

    #join dfSPY with df1
    df1=df1.join(dfSPY)
    print(df1)
    df1=df1.dropna()
    print(df1)


if __name__== "__main__":
    test_run()

