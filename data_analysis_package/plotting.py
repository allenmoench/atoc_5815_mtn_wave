"""
Plots using the data from run_analysis.py

"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def timeseries_plot(x_axis, y_axis, title, xlabel, ylabel, plot_type):
    """
    Plots a timeseries.
    Inputs:
    X-axis: the variable you want on the x-axis (if using a pandas dataframe plotting a timeseries, use df.index.values)
    y-axis: the variable you want on the y-axis
    Title: input desired title
    xlabel: the x-axis label (string format)
    ylabel: the y-axis label (string format)
    plot_type: the plot type (string format). This only works for the plot types I added to the script.
    """
    if plot_type == "scatter":
        plt.scatter(x_axis, y_axis, marker='o', color='steelblue', linewidth=2)
    if plot_type == "plot":
        plt.plot(x_axis, y_axis, marker='', color='steelblue', linewidth=2)


    plt.xlabel(f'{xlabel}')
    plt.ylabel(f'{ylabel}')
    plt.title(f'{title}')
    plt.grid(True, alpha=0.3)


# timeseries_plot(......., 'scatterplot')