import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import data_download as dd
import download_iterator as di
import datetime
import run_analysis as ra
import snotelpy as sp

def anomaly(Day_URL):
    '''
   Takes in  a URL for a single day, and computes a anomaly for temperature.
   Plots observed temperature and temperature anomaly in a dual subplot. 
   
   Parameters
   ----------
   Day_URL : str
        A string containing a URL from ATOC1 station day. 
        
   Returns     
   -------
   df : pandas dataframe
        pandas dataframe from the Day_URL with a updated collumn called ['Temp_Anomaly'] witch contains temperature anomaly
        from choosen date range. 
   
   Notes
   -----
   Could eaisly be modified for other measurements 
    '''
    start_date = datetime.date(2010,11,11)#change for a better longer climatology,
    end_date = datetime.date(2011,1,1)
    comb_df = ra.combined_df(start_date, end_date)#pulls and combines starts and enddates
   

    comb_df['hour'] = comb_df.index.hour #gets each our
    hourly_means = comb_df.groupby('hour')['Temp_Out'].mean()#averages each hour 

    
    df = dd.data_download(Day_URL)
    df['hour'] = df.index.hour
    df['Temp_Climatology'] = df['hour'].map(hourly_means) #maps 14:35 to hour 14 ect
    

    df['Temp_Anomaly'] = df['Temp_Out'] - df['Temp_Climatology'] #observed - expected(for time range)
    
    fig, ax = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
    ax[0].plot(df.index, df['Temp_Out'], color = 'b',label='Observed Temperature F')
    ax[0].set_title(f'ATOC1 Temperature from --> {Day_URL[-12:-4]}')
    ax[0].legend()
    
    
    
    ax[1].bar(df.index, df['Temp_Anomaly'], color = ['red' if v > 0 else 'blue' for v in df['Temp_Anomaly']],width = .003,edgecolor='black')
    ax[1].set_ylabel('Anomaly (°F)')
    ax[1].set_title('Anomaly from Climatology date range(hourly)')
   
    plt.tight_layout()
    plt.show()
    return df


if __name__ == "__main__":
    url = "https://sundowner.colorado.edu/weather/atoc1/wxobs20211230.txt"
    df = anomaly(url)
    