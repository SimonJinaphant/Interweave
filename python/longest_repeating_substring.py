def longest_repeating_substring(line):
    """
    Find the longest repeating substring in a word.

    :param line: The string to find the substring upon
    :return: A substring s where 1 < len(s) < len(word)
    """
    #Build suffix array
    suffix = sorted([line[i:] for i in xrange(len(line))])

    #Compute LCP
    lcp = [None] * len(suffix)
    max_lcp = ""

    for i in xrange(len(suffix)-1):
        left = suffix[i]
        right = suffix[i+1]

        lcp[i+1] = longest_prefix(left, right)
        if len(lcp[i+1]) > len(max_lcp):
            max_lcp = lcp[i+1]

    return max_lcp


def longest_prefix(left, right):
    """
    Find rhe longest common prefix between two strings.

    :return: The longest prefix between the two strings
    """
    for i in xrange(min(len(left), len(right))):
        if left[i] != right[i]:
            return left[0:i]

    return left

print longest_repeating_substring("ababab")