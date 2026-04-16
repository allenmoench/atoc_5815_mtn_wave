"""runs an analysis on the given date range, to pull out trends"""

import pandas as pd

from data_download import data_download
from download_iterator import url_list_compiler as ulc

import datetime

def combined_df(start_date, end_date):
    """
    Loads all data in a given date range as a combined df
    Inputs: 
    Start_date in the format datetime.date(yyyy,m,d)
    End_date in the format datetime.date(yyyy,m,d)
    Outputs: combined dataframe, with rows from all days within the range concatenated together (caution: this could be a lot of data!)
    """
    url_list = ulc(start_date, end_date)
    #print(url_list)
    df1 = data_download(url_list[0])
    #print(df1)
    num_urls = len(url_list)
    for url in url_list[1:num_urls-1]:
        #df1 = pd.DataFrame()
        # print(url)
        df2 = data_download(url)
        comb_df = pd.concat([df1, df2], ignore_index=False)
        df1 = comb_df
    return comb_df

if __name__ == '__main__':
    print("Running tests...")
    start_date = datetime.date(2009,12,20)
    end_date = datetime.date(2010,1,1)
    comb_df=combined_df(start_date, end_date)
    print(comb_df)