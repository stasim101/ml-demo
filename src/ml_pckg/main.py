import pandas as pd


def read_products(filename):
    products = pd.read_csv(filename)
    return products


def main(filename):
    products = read_products(filename)
    data = products.groupby(['SENTIMENT']).size()
    total_value = products['PRODUCT_PRICE'].sum()

    print(data)
    print('Total value:', total_value)


if __name__ == '__main__':
    main('C:\\Users\\IMRAN\\Downloads\\archive\\chunks\\chunk-31.csv')