import matplotlib.pyplot as plt
print("Matplotlib installed successfully!")

# Set up the data
labels = ('Python', 'Scala', 'C#', 'Java', 'PHP')
index = (1, 2, 3, 4, 5)  # provides locations on x axis
sizes = [25, 10, 15, 30, 22]

# Set up the bar chart
plt.bar(index, sizes, tick_label=labels)

# Configure the Layout
plt.ylabel('Usage')
plt.xlabel('Programming Languages')

# Display the chart
plt.show()