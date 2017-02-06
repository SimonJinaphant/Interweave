def word_break(compact_string, dictionary):
    """
    Given a string and a dictionary, return true if string can be split
    into multiple words such that each word is in dictionary

    :param compact_string: The string to test against, it has no spaces
    :param dictionary: Collection of valid words

    :return: True if the input string can be split into multiple valid words
    """

    result = [[None for x in xrange(len(compact_string))] for y in xrange(len(compact_string))]

    def can_break(start, end):
        """
        Given a string, determine if the entire string is a valid dictionary word OR
        it isn't, determine if it can be split into a pair of valid dictionary words

        :param start: Starting index of the string
        :param end: Ending index (non-inclusive) of the string
        :return: True if the string is either a completely valid word OR contains a pair of valid words
        """
        if result[start][end-1] is None:

            # First check if the substring is actually a complete valid word
            if compact_string[start:end] in dictionary:
                result[start][end-1] = (True, start, True)
                return result[start][end-1]

            # The substring isn't a valid word but check if we can split it into a pair of valid words
            for split_index in xrange(end-start-1):
                if can_break(start, start+split_index+1) and can_break(start+split_index+1, end):
                    # The substring can be split into 2 valid dictionary words
                    result[start][end-1] = (True, start+split_index, False)
                    return result[start][end-1]

            # Looks like this substring isn't a valid dictionary word
            result[start][end-1] = False
        else:
            # We already solved this sub-problem earlier, thankfully we cached the result.
            return result[start][end-1]


    """
    Consider the problem for substrings of length 1 to len(compact_string) (inclusive)
        ie: "Iamace" -> "I", "a", "m", "a", "c", "e" for substring length 1
                     -> "Ia", "am", "ma", "ac", "ce" for substring length 2
                     -> ...
                     -> "Iamac", "amace"             for substring length 5
                     -> "Iamace"                     for substring length 6

    """
    for word_size in xrange(1, len(compact_string) + 1):
        for starting_substr in xrange(len(compact_string) - word_size + 1):
            can_break(starting_substr, starting_substr + word_size)

    start = 0
    separable, terminating, whole = result[0][len(compact_string) - 1]
    separated_results = []
    while separable and not whole:
        separated_results.append(compact_string[start:terminating+1])
        start = terminating + 1
        separable, terminating, whole = result[start][len(compact_string) - 1]

    separated_results.append(compact_string[start:])
    return separated_results

for i in word_break("Iamace", {"I", "am", "ace", "a", "ice"}):
    print i,
    
for j in word_break("applepie", {"a", "apple", "orange", "I", "pie"}):
    print j,