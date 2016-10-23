def intersection(list_a, list_b):
    """
    Given two sorted list of numbers, determine the common numbers they share.

    :param list_a: The first list.
    :param list_b: The second list.
    :return: The common elements shared in both lists.
    """
    a = 0
    b = 0
    common = []

    while a < len(list_a) and b < len(list_b):
        if list_a[a] > list_b[b]:
            b += 1
        elif list_a[a] < list_b[b]:
            a += 1
        else:
            common.append(list_a[a])
            a += 1
            b += 1

    return common

