import pandas as pd
import matplotlib.pyplot as plt
import csv


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

    # Remove all values from "Time" column that are less than or equal to 5 and more than or equal to 22
    data = data[(data["Time"] > 5) & (data["Time"] < 22)]

    # Remove all rows with 0 in the "Number of people" column
    data = data[data["Number of people"] != 0]

    # Sort the DataFrame based on the "Number of people" column
    data = data.sort_values(by=["Number of people"], ascending=True)

    # Plot the bar chart with sorted y-axis values
    plt.bar(data["Time"], data['Number of people'])
    plt.xlabel('Time')
    plt.ylabel('Number of People')
    plt.title('Number of people in the pool over time')
    plt.show()


def call(csv_file):
    numbers(csv_file)
    graph(csv_file)

    
call("Sunday.csv")

    




