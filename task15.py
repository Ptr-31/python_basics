# You are working on a project that involves analyzing customer data for a retail company. The data is stored
# in a large CSV file with columns for customer name, product and quantity.
# Each product price is specified in another CSV file.
#
# You should perform the following analysis:
#
#  - Determine the number of unique customers in the data set.
#  - Determine the total number of purchases made by each customer.
#  - Determine the total revenue generated by each customer.

# customer_purchases.csv
# ----------------------
# Customer Name,Item Purchased,Quantity Purchased
# John Doe,Apple,5
# John Doe,Banana,10
# Jane Smith,Orange,7
# Jane Smith,Banana,9
#
# tem_prices.csv
# ---------------
# Item,Price
# Apple,1.00
# Banana,0.50
# Orange,2.00
#
#
# Expected output:
# ----------------
# Number of unique customers: 5
#
# Total purchases made by each customer:
# - John Doe: 21
# - Jane Smith: 24
# - Bob Johnson: 10
# - Sara Lee: 14
# - Samuel Smith: 17
#
# Total revenue generated by each customer:
# - John Doe: $32.00
# - Jane Smith: $34.50
# - Bob Johnson: $7.50
# - Sara Lee: $17.50
# - Samuel Smith: $17.50

import csv

def new_dicts(customer_purchases_csv = 'needed_files/customer_purchases.csv',
              item_prices = 'needed_files/item_prices.csv') -> dict:
    with open(customer_purchases_csv, 'r') as customer_purchases:
        reader = csv.DictReader(customer_purchases)
        names = [row['Customer Name'] for row in reader]
        customer_purchases.seek(0)
        next(customer_purchases)
        unique_names = set(names)
        dictionary_all = {}
        for row in reader:
            if dictionary_all.get(row['Customer Name']) is None:
                dictionary_all[row['Customer Name']] = {}
            if dictionary_all[row['Customer Name']].get(row['Item Purchased']) is None:
                dictionary_all[row['Customer Name']][row['Item Purchased']] = int(row['Quantity Purchased'])
            else:
                dictionary_all[row['Customer Name']][row['Item Purchased']] += int(row['Quantity Purchased'])
        # print(dictionary_all)
        print('Number of unique clients:', len(dictionary_all))
        return dictionary_all
def analytics(dictionary_all: dict, item_prices_csv = 'needed_files/item_prices.csv'):
    with open(item_prices_csv, 'r') as item_prices:
        reader = csv.DictReader(item_prices)
        prices = {row['Item']: float(row['Price']) for row in reader}
    for person in dictionary_all:
        temp_revenue = 0
        temp_purchases = 0
        for item in dictionary_all[person]:
            temp_purchases += int(dictionary_all[person][item])
            temp_revenue += dictionary_all[person][item] * prices[item]
        print(person, 'has', temp_purchases, 'purchases and total revenue = ', temp_revenue)
def main():
    analytics(new_dicts())

if __name__ == '__main__':
    main()