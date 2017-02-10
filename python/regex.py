def regex_match(text, pattern):
    """

    :param text:
    :param pattern:
    :return:
    """

    """
    At cell T[i][j], we store the result if @text[:i] matches @pattern[:j]
    """
    result = [[False for x in xrange(len(pattern)+1)] for y in xrange(len(text)+1)]

    # Empty string matches empty pattern
    result[0][0] = True

    # We have an offset of 1 in our table so when we index text or pattern we have to go one spot back
    for i in xrange(1, len(text)+1):
        for j in xrange(1, len(pattern)+1):

            # They both match on the rightmost character
            # The result now depends on the previous subproblem where the rightmost were not included
            if text[i-1] == pattern[j-1] or pattern[j-1] == ".":
                result[i][j] = result[i-1][j-1]

            elif pattern[j-1] == "*":

                # Check if they match for 1 occurrence of the previous character by solving the sub-problem
                # when the previous text is compared to the current pattern but only
                # if the rightmost text character match the previous pattern character
                if text[i-1] == pattern[j-2] or pattern[j-2] == ".":
                    result[i][j] = result[i-1][j]

                # Otherwise check if they match for 0 occurrence of the previous character by solving the sub-problem
                # when current text is compared to the pattern but without the previous character
                # which involves jumping 2 spaces back in our table (one for the *, another for the character)
                else:
                    result[i][j] = result[i][j-2]

    for row in result:
        print row

    return result[-1][-1]

print regex_match("xaabyc", "xa*b.c")