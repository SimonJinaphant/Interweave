from math import ceil

def word_break(compact_string, dictionary):
    """
    Given a string and a dictionary, return true if string can be split
    into multiple words such that each word is in dictionary

    :param compact_string: The string to test against, it has no spaces
    :param dictionary: Collection of valid words

    :return: True if the input string can be split into multiple valid words
    """

    result = [[None] * len(compact_string) ] * len(compact_string)

    def can_break(start, end):
        """

        :param start: Starting index
        :param end: Ending index (non-inclusive)
        :return:
        """
        print compact_string[start:end]


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


    print result





word_break("Iamace", {"I", "am", "ace", "a", "ice"})