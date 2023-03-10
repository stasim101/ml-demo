import pandas as pd
import numpy
import matplotlib.pyplot as plot


def read_products(filename):
    products = pd.read_csv(filename)
    return products


def main(filename):
    products = read_products(filename)
    data = products.groupby(['Category']).size().to_dict()

#    x = data.keys()
#    y = data.values()

    x = numpy.random.normal(5.0, 1.0, 1000)
    y = numpy.random.normal(10.0, 2.0, 1000)

    plot.scatter(x, y)
    plot.title('Walmart Sales Analysis')
    plot.xlabel('Categories')
    plot.ylabel('Sales Count')
    plot.show()


if __name__ == '__main__':
    main('D:\\Python code\\Data\\Walmart Sales Analysis\\Walmart.csv')