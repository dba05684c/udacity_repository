"""
The script takes a file with a list of prices.
It searches for all the prices below 25
Sums them and adds a tax, before returning the total

Author:  Jan

Date: 2024-06-12

"""
import numpy as np


def get_total_price(source_path):
    """
    Function: get_total_price

    Parameters:
        source_path: (str) path containing list of numbers

    Returns:
        v_total_price: (int)
    """
    with open(source_path, encoding="utf-8") as file_source:
        gift_costs = file_source.read().split('\n')

    # convert string to int
    gift_costs = np.array(gift_costs).astype(int)

    # calculate and take in account taxes
    v_total_price = (gift_costs[gift_costs < 25]).sum() * 1.08

    return v_total_price


if __name__ == '__main__':
    TOTAL_PRICE = 0
    TOTAL_PRICE = get_total_price('gift_costs.txt')
    print(f"The total price = {TOTAL_PRICE}")
