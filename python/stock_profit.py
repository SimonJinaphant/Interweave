def stockmarket(stock_prices):
    """
    Given the daily stock prices of a stock; determine the maximum profit that can be obtained buying and selling it.

    :param stock_prices: List of positive integers representing the price of a stock.
    :return: The buy and sell value for maximum profit.
    """

    """
    Consider a divide and conquer approach; we can split the problem into two halves and solve it for those two, followed
    by combining the two results again to form the original answer.

    Basecase: A one element stock price is both its min and max

    Find the min/max pair of a given subarray, then take those min/max and compare them against each other to take the
    min/max of those pairs.
    """
    if len(stock_prices) == 1:
        return (stock_prices[0], stock_prices[0])

    mid = len(stock_prices) / 2

    left_min_max = stockmarket(stock_prices[0:mid])
    right_min_max = stockmarket(stock_prices[mid:])

    return (min(left_min_max[0], right_min_max[0]), max(left_min_max[1], right_min_max[1]))


print stockmarket([10, 7, 5, 8, 11, 9])