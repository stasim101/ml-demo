import pandas as pd
import numpy
import matplotlib.pyplot as plot


def read_products(filename):
    products = pd.read_csv(filename)
    return products


def main(filename):
    products = read_products(filename)
    data = products.groupby(['Category']).size().to_dict()

    x = data.keys()
    y = list(data.values())

    y_mean = numpy.mean(y)
    y_std = numpy.std(y)
    y_len = len(y)

    y_a = numpy.random.normal(y_mean, y_std , y_len)

    plot.scatter(x, y_a)
    plot.title('Walmart Sales Analysis')
    plot.xlabel('Categories')
    plot.ylabel('Sales Count')
    plot.show()


if __name__ == '__main__':
    main('D:\\Python code\\Data\\Walmart Sales Analysis\\Walmart.csv')