# Plotting graphs in Python

# import the relevant modules
import matplotlib.pyplot as plt         # named the package plt

# create a very basic plot - we'll want something better
# create a random list
x = [1, 3, 5, 10]   # this is what we're plotting
plt.plot(x)         # this won't work because you need to say --> plt.show()
plt.show()          # v basic, no axis or labels, press red stop button to stop running the graph

# plotting x & y against each other
# both lists need to have the same no of entries
y = [7, 12, 21, 22]
plt.plot(x, y)      # +ive correlation as x increases, y increases
plt.show()




# build a better plot

# import the relevant modules
import matplotlib.pyplot as plt         # named the package plt

# line 1 - points
x = [3, 9, 14]
y = [2, 7, 30]
# plotting x & y
# now inc info on how you want the graph to look
plt.plot(x, y, c="red", linewidth=2, label="Line 1")
# plt.show()      # no legend (i.e key) has popped up, as you have to ask python to recall it

# Line 2 - points
x2 = [1, 15, 18]
y2 = [0, 3, 12]
# plotting x & y
plt.plot(x2, y2, c="green", linewidth=0.5, label="Line 2")
# plt.show()

# label the axis & title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Table one!")

# show the legend (i.e. key) on the plot --> this will show the labels given to each plot L26, L33
plt.legend()

# get python to show the plot
plt.show()




# other styles to add on a graph

# import the relevant modules
import matplotlib.pyplot as plt         # named the package plt

# line 1
a = [3, 9, 14]
b = [2, 7, 30]
# plotting a & b
# now inc info on how you want the graph to look
plt.plot(a, b, c="pink", linewidth=2, label="Line 1")

# Line 2 - points
a2 = [1, 15, 18]
b2 = [0, 3, 12]
# plotting a2 & b2
plt.plot(a2, b2, c="blue", linewidth=0.5, label="Line 2", linestyle="dashed",
         marker='o', markerfacecolor="black", markersize=10)
# if marker='s' then the marker will be a square


plt.xlabel("A-axis")         # label the axis & title
plt.ylabel("B-axis")
plt.title("Table two!")

# limits of the axis
plt.xlim(0, 30)         # limit between 0 & 30
plt.ylim(1, 10)         # limit between 1 & 10

plt.legend()        # show the legend (i.e. key) on the plot
plt.show()




# Create a graph with two lines

import matplotlib.pyplot as plt

# line 1 points
x = [12, 23, 32, 46, 54, 71, 98]
y = [17, 28, 35, 52, 69, 99, 74]
plt.plot(x, y, c="purple", linewidth=2, label="Line 1", marker='s', markerfacecolor="yellow",
         markersize=6)

# line 2 points
x2 = [19, 26, 34, 49, 58, 67, 86]
y2 = [22, 38, 43, 59, 64, 71, 92]
plt.plot(x2, y2, c="orange", linewidth=2, label="Line 2", linestyle="dashed",
         marker='o', markerfacecolor="black", markersize=6)

plt.xlabel("X-axis")         # label the axis & title
plt.ylabel("Y-axis")
plt.title("A Random Graph")

plt.legend()        # show the legend (i.e. key) on the plot
plt.show()
