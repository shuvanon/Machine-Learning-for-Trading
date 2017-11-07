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


if __name__== "__main__":
    test_run()

