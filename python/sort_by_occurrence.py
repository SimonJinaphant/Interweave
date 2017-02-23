def sort_by_occurrence(message):
    """
    Sort a given string by the number of letter occurences

    ex: Aabb -> bbAa since 'b' appears twice, while 'A' and 'a' only appears once
        aabccc -> cccaab since 'c' appears 3 times, 'a' 2 times, ..etc..

    :param message: The message to sort
    :return: String with the most repeated characters all at the front
    """

    # Count all occurrences of a letter
    occurences = {}
    max_occurence = 1
    for letter in message:
        if letter in occurences:
            occurences[letter] += 1
            max_occurence = max(max_occurence,occurences[letter])
        else:
            occurences[letter] = 1

    # Create buckets to hold letters of 1 occurrence to @max_occurrences occurrence
    buckets = [[] for i in xrange(max_occurence+1)]

    # Add the letters to their corresponding buckets
    for k,v in occurences.iteritems():
        buckets[v].append(k*v)

    # Reduce the buckets into one in a reversed manner
    result = []
    for bucket in reversed(buckets):
        if len(bucket) != 0:
            result.extend(bucket)

    return "".join(result)


print sort_by_occurrence("Aabb")
