import sesd
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

from prepare_data import prepare_data


def plot(data, marks, number_of_outliers):
    plt.figure(figsize=(24, 10))
    plt.plot(data, color="green", linestyle='-', label='Time series')
    plt.plot(marks, 'r*', markersize="4", label='Anomaly')
    red_patch = mpatches.Patch(color='red', label='Anomaly')
    green_lines = mpatches.Patch(color='green', label='Time series')
    plt.legend(handles=[green_lines, red_patch])
    plt.title(f'Founded anomaly date: {number_of_outliers}')
    plt.ylabel('Temperature')
    plt.xlabel('Time series')
    plt.grid(True)
    plt.show()


def shesd(data, max_anomalies, alpha):
    marks = []
    outliers = []
    number_of_outliers = 0
    outliers_indices = sesd.seasonal_esd(data, hybrid=True, max_anomalies=max_anomalies, alpha=alpha)
    for idx in outliers_indices:
        outliers.append(data[idx])
    for i in data:
        if i in outliers:
            marks.append(i)
            number_of_outliers += 1
        else:
            marks.append(None)
    plot(data, marks, number_of_outliers)


prepare_data('weatherULURU.csv')
df = pd.read_csv("file.csv")
df = df['temperature']
shesd(df, 100, 0.1)