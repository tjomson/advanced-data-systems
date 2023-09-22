#%%
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv("data.csv")

# Extract the data columns
x = df.iloc[:, 0]  # Assuming the first column is the x-axis data
y = df.iloc[:, 1:]  # Assuming the remaining columns are y-axis data

# Define a list of 22 distinct colors for the lines
line_colors = [
    'b', 'g', 'r', 'c', 'm', 'y', 'k',  # Basic colors
    'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan',  # Tab colors
    'darkorange', 'limegreen', 'dodgerblue', 'gold', 'firebrick'  # Additional colors
]

# Plot the data using a loop for each y-axis column
plt.figure(figsize=(12, 8))  # Adjust the figure size if needed

for i, column in enumerate(y.columns):
    color = line_colors[i % len(line_colors)]  # Get a color from the list
    plt.plot(x, y[column], label=f'Column {column}', color=color)
    
    # Add labels to the right of each line with the same color
    plt.text(x.iloc[-1] + 0.1, y[column].iloc[-1], f'Column {column}', color=color, verticalalignment='center')

plt.title('tpc-h benchmark')
plt.xlabel('scale factor')
plt.ylabel('time (s)')
plt.grid(True)

plt.show()
