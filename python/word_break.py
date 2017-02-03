from math import ceil

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

        :param start: Starting index
        :param end: Ending index (non-inclusive)
        :return:
        """
        print compact_string[start:end]
        if result[start][end-1] == None:
            if end - start == 1:
                #Basecase: single letter
                result[start][end-1] = compact_string[start:end] in dictionary
                return result[start][end-1]

            if compact_string[start:end] in dictionary:
                result[start][end-1] = True
                return result[start][end-1]

            split_result = False
            for split_index in xrange(end-start-1):
                left_substring = compact_string[start:start+split_index+1]
                right_substring = compact_string[start+split_index+1: end]

                #print "\t{0}, {1} & {2}".format(compact_string[start:end], left_substring, right_substring)
                split_result = can_break(start, start+split_index+1) and can_break(start+split_index+1, end)
                if split_result:
                    result[start][end-1] = True
                    return result[start][end-1]

            result[start][end-1] = False
        else:
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


    for row in result:
        print row





word_break("Iamace", {"I", "am", "ace", "a", "ice"})