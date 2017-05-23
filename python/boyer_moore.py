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
            # j represents how many characters are to the right of the current pattern

            if patternLetter != text[i+j]:
                if text[i+j] not in skiptable:
                    '''
                    Since we mismatched on a character that's not in the pattern we can shift the entire pattern to the
                    right until we passed the mismatched character since its impossible for any matches until we
                    completely move pass it.
                    '''
                    skip = j+1
                else:
                    '''
                    Otherwise if the mismatched character in the text is actually a character in the pattern then we'll
                    slide the pattern over a couple of spaces until they both are aligned with the same letter.

                    ex:
                    Text:           aneedleinahaystack
                    Pattern:        needle

                    On first check the text's `l` and the pattern's `e` mismatched but since `l` is also a character in
                    the pattern, we'll slide the pattern over until the pattern's l is aligned with the text's l and
                    restart the match checking again.
                    '''
                    skip = max(1, j - skiptable[text[i+j]])
                break

        if skip == 0:
            # No mismatched occurred; we've successfully found a substring!
            return i+j

        # Update the starting position of the text to align with how many character's we've skipped in the pattern.
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
