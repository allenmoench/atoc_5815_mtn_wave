import data_download #edit
import datetime

def url_list_compiler(start_date, end_date):
    """
    Iterates through all weather data files.
    Input: Data download function
        start_date = a start date, in the format of datetime.date(yyyy,m,d)
        end_date = an end date, in the format of datetime.date(yyyy,m,d)
    Output: A combined dataframe
    """
    # how to make a datetime into a string:
    # start_date = datetime.date(start_date) # datetime.date(year, month, day)
    next_date = start_date + datetime.timedelta(days=1) # (start date + "add one day")
    # end_date = datetime.date(end_date)
    # num_days = end_date - start_date #num_days.days gives the number of days as an integer
    # strftime("%Y%m%d")
    date_range = [start_date]
    while (start_date <= end_date):
        next_date = start_date + datetime.timedelta(days=1) # (start date + "add one day")
        date_range.append(next_date)
        start_date = next_date
    
    # print(date_range)

    url_list = []
    for date in date_range: # this won't work, because url_list is empty, so there's nothing to iterate through. 
        date_str = str(date).replace("-", "")
        url = f"https://sundowner.colorado.edu/weather/atoc1/wxobs{date_str}.txt"
        url_list.append(url)
    #print(url_list)
    return url_list
    # for url in url_list: # note: I might want to do this part later, in the combined document.
    #     data_download(url)



if __name__ == "__main__":
    print("Running tests...")
    start_date = datetime.date(2009,12,20)
    end_date = datetime.date(2010,1,1)
    print(url_list_compiler(start_date, end_date))
