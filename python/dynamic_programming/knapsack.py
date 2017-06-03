def knapsack(capacity, items):
    """
    Given a collection of items with a value and weight, determine the best set of items to take which maximizes value
    while staying under a weight capacity.

    :param capacity: Positive integer denoting the weight capacity the bag can hold
    :param items: Collection of 2D tuples denoting (weight, value)
    :return:
    """

    """
    This is a famous Dynamic Programming problem; we want to maximize the profit while staying under our capacity.
    The limiting factor is the weight, we have to stop when we go over our capcity.

    We can consider a 2D table, where each row represents the next largest weight of item we can take, and the columns
    as the total capacity.

    Given the following tuples of item's value and weight:
        (1,1), (3,4), (4,5), (5,7)
    and a weight capacity of 7, we construct a table with 4 rows (1 per item) and 7 + 1 columns (for 0 to max capacity)
    """
    result = [[None for x in xrange(capacity+1)] for y in xrange(len(items))]


    """
    We'll handle the base cases first; on the first row we'll place 0 for any cell with column index less than the
    current row's item weight. ie: We place 0 because its impossible to earn any profit with a weight capacity that's under
    the smallest item's weight.

    We'll also put 0 for all the colums in index 0 since we cannot take any items with a capacity of 0.
    """
    # Fill in the first row and column to state the basecase
    first_weight, first_value = items[0]
    for x in xrange(capacity+1):
        if x < first_weight:
            result[0][x] = 0
        else:
            result[0][x] = first_value

    for y in xrange(len(items)):
        result[y][0] = 0


    """
    Now for the dynamic programming part:
    We'll iterate through each open cells:

        If the current row's item weight cannot fit into the current capacity, we'll ignore the item and copy down the
        previous row's value for that column.

        Otherwise we'll consider the maximum of two values: The previous row's value (ie we dont take the current item)
        compared with the current row's value + the previous sub-problem for the new weight capacity.
    """
    for i in xrange(1, len(items)):
        for j in xrange(1, capacity+1):
            weight, value = items[i]

            if weight > j:
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = max(value+result[i-1][j-weight], result[i-1][j])

    """
    With a completed table of values for each sub-problem we can now construct our final answer by working backwards
    with the cell's value, starting at the last cell we updated.

    We look one row up to see if the numbers are the same, if so this means the current row's item wasn't taken and we'll
    move up by one row to check if another row's item can be taken.

    Otherwise if we took the current row's item we'll shift one row up and X collumns left, where X is the row item's
    weight, effectively solving a sub-problem for a new capacity.

    We keep doing this until we pass the first row.
    """
    # Determine which items to put into our bag now
    i = len(items)-1
    j = capacity
    loot_bag = []

    while i > 0:
        if result[i][j] == result[i-1][j]:
            # We didn't take this item
            i -= 1
        else:
            # We took the item
            loot_bag.append(items[i])
            j -= items[i][0]
            i -= 1

    # Remember to add the row item if we still have room!
    if j != 0:
        loot_bag.append(items[0])

    return loot_bag

print knapsack(7, [(1,1), (3,4), (4,5), (5,7)])