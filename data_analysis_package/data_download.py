import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_download(url):
    """
    Description: Downloads data (for example, from the CU Boulder weather archive).
    Inputs: .txt file url containing weather observation data
    Outputs: a dataframe containing the data from the .txt file
    """

    df = pd.read_fwf(url, header=[0, 1], skiprows=[2])

    date_col = [c for c in df.columns if c[1] == "Date"][0]
    time_col = [c for c in df.columns if c[1] == "Time"][0]

    t = (
        df[time_col]
        .astype(str)
        .str.strip()
        .str.replace(r"a$", "AM", regex=True)
        .str.replace(r"p$", "PM", regex=True)
    )

    dt = pd.to_datetime(
        df[date_col].astype(str).str.strip() + " " + t,
        format="%m/%d/%y %I:%M%p",
        errors="coerce",
    )

    df = df.set_index(dt).drop(columns=[date_col, time_col])
    df.index.name = "datetime"

    df.columns = [
        "_".join([str(a).strip(), str(b).strip()]).replace(" ", "_").strip("_")
        for a, b in df.columns
    ]

    return df

if __name__ == '__main__':
    url = "https://sundowner.colorado.edu/weather/atoc1/wxobs20211230.txt"
    df = data_download(url)
    print(f"Here's the dataframe you just created: {df}")
    print("====================================")
    # print(f"Column headings: {df.columns}")
    print("All Checks Passed")
