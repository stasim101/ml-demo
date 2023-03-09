import pandas as pd
import matplotlib.pyplot as plt

def read_products(filename):
    products = pd.read_csv(filename)
    return products


def main(filename):
    products = read_products(filename)
    data = products.groupby(['Category']).size()

#    print(data.to_dict().keys())
    x_axis = data.to_dict().keys()
    y_axis = data.to_dict().values()

    plt.bar(x_axis, y_axis)
    plt.title('Walmart Sales Analysis')
    plt.xlabel('Categories')
    plt.ylabel('Sales Count')
    plt.show()


if __name__ == '__main__':
    main('D:\\Python code\\Data\\Walmart Sales Analysis\\Walmart.csv')