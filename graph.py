import pandas as pd
import matplotlib.pyplot as plt
import csv
from matplotlib.pyplot import figure
import numpy as np


# necessary to display the y axis in the correct order
def numbers(csv_file):
    with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            your_list = list(reader)

    for i in range(len(your_list)):
            for j in range(len(your_list[i])):
                if len(your_list[i][j]) == 1:
                    your_list[i][j] = "00" + your_list[i][j]
                elif len(your_list[i][j]) == 2:
                    your_list[i][j] = "0" + your_list[i][j]

    with open(csv_file, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(your_list)


    # Read the CSV file into a pandas DataFrame and remove every odd row
def graph(csv_file):
    data = pd.read_csv(csv_file)
    data = data.iloc[::2, :]

    # Convert the "Time" column to numerical values
    data["Time"] = pd.to_numeric(data["Time"])
    data["Number of people"] = pd.to_numeric(data["Number of people"])
    # Remove all values from "Time" column that are less than or equal to 5 and more than or equal to 22
    data = data[(data["Time"] > 5) & (data["Time"] < 22)]

    # Remove all rows with 0 in the "Number of people" column
    data = data[data["Number of people"] != 0]

    # Sort the DataFrame based on the "Number of people" column
    data = data.sort_values(by=["Number of people"])

    figure(figsize=(20, 18))
    
    bars = plt.bar(data["Time"], height=data["Number of people"])

    # Plot the bar chart with sorted y-axis values
    plt.xlabel('Time',fontsize=14)
    plt.ylabel('Number of People', fontsize=14)
    plt.title('Number of people in the pool over time',fontsize=14)

    for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x(), yval+1, yval, fontsize=14)
    plt.show()


def call(csv_file):
    numbers(csv_file)
    graph(csv_file)

    
call("Saturday.csv")

    




