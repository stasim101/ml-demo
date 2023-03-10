import numpy
import matplotlib.pyplot as plt
from scipy import stats

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]


def main():
    model = numpy.poly1d(numpy.polyfit(x, y, 3))
    line = numpy.linspace(1, 33, 100)
    plt.scatter(x, y)
    plt.plot(line, model(line))
    plt.show()


if __name__ == '__main__':
    main()
