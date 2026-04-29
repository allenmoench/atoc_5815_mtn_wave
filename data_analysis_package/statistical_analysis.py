"""
Description: 
Produces plots to examine statistical characteristics of particular variables in a weather dataset
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from plotting import timeseries_plot as tp

import data_download as dd
import download_iterator as di
import datetime
import run_analysis as ra

import seaborn as sb

def simple_timeseries (url, start_date, end_date, column_name):
    """
    Creates a timeseries plot for a variable defined by a column name, over a given period of time.
    Arguments:
    url: the url for the data file, in the format "http://...<yyyymmdd>.txt"
    start_date: a start date, in the format of datetime.date(yyyy,m,d)
    end_date: an end date, in the format of datetime.date(yyyy,m,d)
    column_name: The exact name of the column to be plotted, eg. "Out_Temp", "Out_Hum"
    Outputs: a timeseries plot.
    """
    url = url
    dd.data_download(url)
    start_date = start_date
    end_date = end_date

    df = ra.combined_df(start_date, end_date)

    count=0
    count_int=0
    for ii,vv in enumerate(df[column_name]):
        if type(vv)==int:
            count_int+=1
        continue
    else:
        # print(vv, type(vv),ii)
        count+=1
    # print(count, count_int)    

    for x in df[column_name]:
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    # print(df["Temp_Out"])
    
    plt.plot(df[column_name])

    time = df.index.values

    variable = df[column_name]

    # print(df.index.dtype())
    # print(time, temperature)

    plt.figure(figsize=(12,3))
    plt.plot(time, column_name, marker='o', color='steelblue', linewidth=2)
    plt.xlabel('Time')
    plt.ylabel(column_name)
    plt.title(f'{column_name} over time')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.show

def mean_plot(url, start_date, end_date, column_name, timestep):
    """
    Creates a timeseries plot for mean of a variable over a given timestep defined by a column name, over a given period of time.
    Arguments:
    url: the url for the data file, in the format "http://...<yyyymmdd>.txt". Note: don't worry if the date in the URL is incorrect - the script will replace it with the start and end dates.
    start_date: a start date, in the format of datetime.date(yyyy,m,d)
    end_date: an end date, in the format of datetime.date(yyyy,m,d)
    column_name: The exact name of the column to be plotted, eg. "Out_Temp", "Out_Hum"
    timestep: The timestep over which you want the mean (eg. month, year)
    """
    url = url
    dd.data_download(url)
    start_date = start_date
    end_date = end_date
    ts = column_name.groupby(timestep) #Note: need to figure out how to incorporate this

    df = ra.combined_df(start_date, end_date)

    count=0
    count_int=0
    for ii,vv in enumerate(df[column_name]):
        if type(vv)==int:
            count_int+=1
        continue
    else:
        # print(vv, type(vv),ii)
        count+=1
    # print(count, count_int)    

    for x in df[column_name]:
        df[column_name] = pd.to_numeric(df[column_name], errors='coerce')
    # print(df["Temp_Out"])
    
    plt.plot(df[column_name])

    time = df.index.values

    # print(df.index.dtype())
    # print(time, temperature)
    plt.figure(figsize=(12,3))
    plt.plot(time, ts, marker='o', color='steelblue', linewidth=2)
    plt.xlabel('Time')
    plt.ylabel(f"mean {column_name}")
    plt.title(f'Mean {column_name} over time')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.show

if __name__ == '__main__':
    print("Running tests...")
    column_name = "Hi_Speed"
    url = "https://sundowner.colorado.edu/weather/atoc1/wxobs20211230.txt"
    start_date = datetime.date(2021,12,1)
    end_date = datetime.date(2021,12,31)
    timeseries = simple_timeseries(column_name, url, start_date, end_date)
    print(f"Windspeed plot: {timeseries}")