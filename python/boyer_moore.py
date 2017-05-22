import unittest


def substring(text, pattern):
    """Determines the first index where the pattern occurs in a given text

    :param text: The text to query
    :param pattern: The pattern to match in text
    :return: The first index where the pattern matched, otherwise None if no pattern was found
    """

    N = len(text)
    M = len(pattern)

    # It makes no sense for a pattern query to be longer than the actual text.
    if M > N:
        return False

    #Build skip table
    skiptable = {letter: i for i, letter in enumerate(pattern)}

    skip = 0
    i = 0
    
    while i <= N - M:
        skip = 0
        '''
        Compare by aligning the text and pattern on the left, and starting from the right
        Text:           a b e d a b c
        Pattern:        a b c

        First compare c and e, then b and b, then a and a
        '''

        for j, patternLetter in reversed(list(enumerate(pattern))):
            if patternLetter != text[i+j]:
                if text[i+j] not in skiptable:
                    '''
                    Since we mismatched on a character that's not in the pattern we can shift the entire pattern to the
                    right until we passed the mismatched character since its impossible for any matches until we pass it.
                    '''
                    skip = j+1
                else:
                    '''
                    Otherwise we'll skip between 1 and the length of the pattern
                    '''
                    skip = max(1, j - skiptable[text[i+j]])
                break

        if skip == 0:
            return i+j

        i += skip
    
    return None


class TestBoyerMoore(unittest.TestCase):

    def test_ends(self):
        self.assertEqual(substring("abedabc","abc"), 4)
        self.assertEqual(substring("carpet", "car"), 0)

    def test_normal(self):
        self.assertEqual(substring("aneedleinahaystack", "needle"), 1)

    def test_absent(self):
        self.assertEqual(substring("java", "ada"), None)

if __name__ == "__main__":
    unittest.main()
