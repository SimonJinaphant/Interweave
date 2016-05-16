from copy import deepcopy


def powersets(elements, current):
    """Generate a set of all subset

    :param elements: A set of elements
    :param current: The current index to permute on
    :return: A set containing all subsets of the input set
    """
    if len(elements) == current:
        return [[]]

    subset_previous = powersets(elements, current + 1)
    subset_current = deepcopy(subset_previous)

    for sub in subset_current:
        sub.append(elements[current])

    #Using extends() seems to cause unexpected behavior with nested lists
    new_subset = subset_previous
    for sub in subset_current:
        new_subset.append(sub)

    return new_subset


print powersets([1, 2, 3], 0)