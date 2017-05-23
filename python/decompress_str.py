import unittest


def decompress_str(compressed):
    """
    A string has been compressed finely such that repeated sequences are shortened by a number.

    Example:
        aaabcbc -> 3[a]2[bc]
        accaccacc -> 3[a2[c]]
        abcabccdcdcdef -> 2[abc]3[cd]ef

    Reverse the compression and restore the original uncompressed string.
    You may assume the input string is always valid such
    that there's no white space, extra/missing brackets, etc..

    :param compressed: The compressed string with the format k[str] where str is repeated k times
    :return: The uncompressed string
    """

    """
    Consider analysing the problem from right to left as we do with string problems which require us to expand it.

    We'll add the letters into a collection and then once we encounter a number we'll take all the letters accumulated
    so far and multiply it before putting it back into the collection.

    The [ bracket will be useless as there will always be a number to the left of it which denotes the need to start
    expanding character's we accumulated so far; therefore the ] bracket will be used to signal the end of the expansion
    """
    character_stack = []
    black_list = set([str(i) for i in xrange(10)])

    for character in reversed(compressed):

        if character == "[":
            continue

        if character not in black_list:
            character_stack.append(character)
        else:
            sub_string = []
            while character_stack[-1] != "]":
                sub_string.append(character_stack.pop())
            character_stack.pop()

            character_stack.append(int(character) * "".join(sub_string))

    # Reverse the collection to form the proper string since we've been adding it backwards.
    final_str = []
    while len(character_stack) != 0:
        final_str.append(character_stack.pop())

    return "".join(final_str)


class TestDecompress(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(decompress_str("3[a2[c]]"), "accaccacc")
        self.assertEqual(decompress_str("3[a]2[bc]"), "aaabcbc")
        self.assertEqual(decompress_str("2[abc]3[cd]ef"), "abcabccdcdcdef")


if __name__ == "__main__":
    unittest.main();