def knapsack(capacity, items):
    """

    :param capacity: Positive integer denoting the weight capacity the bag can hold
    :param items: Collection of 2D tuples denoting (weight, value)
    :return:
    """

    result = [[None for x in xrange(capacity+1)] for y in xrange(len(items))]

    # Fill in the first row and column to state the basecase
    first_weight, first_value = items[0]
    for x in xrange(capacity+1):
        if x < first_weight:
            result[0][x] = 0
        else:
            result[0][x] = first_value

    for y in xrange(len(items)):
        result[y][0] = 0

    for i in xrange(1, len(items)):
        for j in xrange(1, capacity+1):
            weight, value = items[i]

            if weight > j:
                result[i][j] = result[i-1][j]
            else:
                result[i][j] = max(value+result[i-1][j-weight], result[i-1][j])

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

    if j != 0:
        loot_bag.append(items[0])

    return loot_bag

print knapsack(8, [(1,1), (3,4), (4,5), (5,7)])