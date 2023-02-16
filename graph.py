import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame and remove every odd row
data = pd.read_csv("Friday.csv")
data = data.iloc[::2, :]

# Convert the "Time" column to numerical values
data["Time"] = pd.to_numeric(data["Time"])

# Remove all values from "Time" column that are less than or equal to 5 and more than or equal to 22
data = data[(data["Time"] > 5) & (data["Time"] < 22)]

# Remove all rows with 0 in the "Number of people" column
data = data[data["Number of people"] != 0]

# Sort the DataFrame based on the "Number of people" column
data = data.sort_values(by=["Number of people"])

# Assign a unique rank to each value in the "Number of people" column, UPDATE: commented out as useless for now
#data["Rank"] = data["Number of people"].rank(method="dense")

# Plot the bar chart with sorted y-axis values
plt.bar(data["Time"], data['Number of people'])
plt.xlabel('Time')
plt.ylabel('Number of People')
plt.title('Number of people in the pool over time')
plt.show()

# Save the plot to a file
plt.savefig("your_graph.png")
