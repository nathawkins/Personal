import argparse
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()

parser.add_argument("data", help = "the data you want to plot")

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help = 'designates the input as a file, text file required', action = "store_true")
group.add_argument("-l", "--list", help = "designates the input as a list", action = "store_true")

plots = parser.add_mutually_exclusive_group()
plots.add_argument("-H", "--hist", help ="makes a histogram of the data", action = "store_true")
plots.add_argument("-L", "--line", help = "makes a lineplot of the data", action = "store_true")
plots.add_argument("-S", "--scatter", help = "makes a scatterplot of the data", action = "store_true")
plots.add_argument("-B", "--bar", help = "makes a bar chart of the data", action = "store_true")

args = parser.parse_args()

if args.list:
    data = []
    for i in list(args.data):
        try:
            val = float(i)
            data.append(val)
        except:
            continue

elif args.file:
    print("Loading data from '{}'".format(args.data))
    data = np.loadtxt(args.data, delimiter = ",")

else:
    print("Data not obtained")


if args.hist:
    print("Histogram")
    plt.hist(data)
    plt.show()

elif args.line:
    print("Line")
    plt.plot(data, "b-")
    plt.show()

elif args.scatter:
    print("Scatter")
    plt.plot(data, "bp")
    plt.show()

elif args.bar:
    print("Bar")
    plt.bar(range(len(data)), data)
    plt.show()

else:
    print("No visualization could be made")
