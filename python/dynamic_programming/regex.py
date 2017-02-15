import unittest


def regex_match(text, pattern):
    """
    Determine if the given text matches the pattern using simple regex including:
        . (for any single character)
        * (for 0 or more character)

    :param text: The text to compare
    :param pattern: The pattern to check against the text
    :return: True if the given text matches the pattern
    """

    # At cell T[i][j], we store the result if @text[:i] matches @pattern[:j]
    result = [[False for x in xrange(len(pattern)+1)] for y in xrange(len(text)+1)]

    # Empty string matches empty pattern
    result[0][0] = True

    # Special case patterns like comparing "" with "a*" or "" with "a*b*" or "" with "a*b*c*" etc..
    for x in xrange(1, len(pattern)+1):
        if pattern[x-1] == "*":
            result[0][x] = result[0][x-2]

    # We have an offset of 1 in our table so when we index text or pattern we have to go one spot back
    for i in xrange(1, len(text)+1):
        for j in xrange(1, len(pattern)+1):

            # They both match on the rightmost character
            # The result now depends on the previous subproblem where the rightmost were not included
            if text[i-1] == pattern[j-1] or pattern[j-1] == ".":
                result[i][j] = result[i-1][j-1]

            elif pattern[j-1] == "*":
                # Check for the case of 0 occurrence by comparing current text
                # to the pattern without '*' and its preceding letter.
                result[i][j] = result[i][j-2]

                # Additionally check for the case of 1+ occurrence if the preceding pattern letter matches
                # by comparing the text without its matched rightmost character to the same pattern
                # "aa" compare with "a*" will depend on "a" compare with "a*" and thus "" with "a*"
                if text[i-1] == pattern[j-2] or pattern[j-2] == ".":
                    result[i][j] |= result[i-1][j]

    return result[-1][-1]


class RegexMatchingTest(unittest.TestCase):

    def test_normals(self):
        self.assertEqual(regex_match("xaabyc", "xa*b.c"), True)
        self.assertEqual(regex_match("abc", "a.c"), True)

    def test_basic(self):
        self.assertEqual(regex_match("a", "a"), True)
        self.assertEqual(regex_match("abc", "abc"), True)

        # Match any single character
        self.assertEqual(regex_match("a", "."), True)

        # Match any character 0 or more time
        self.assertEqual(regex_match("aaa", "a*"), True)
        self.assertEqual(regex_match("aaa", ".*"), True)


if __name__ == "__main__":
    unittest.main()
