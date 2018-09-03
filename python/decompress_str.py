import unittest


def decompress_str(compressed):
    """
    A string has been compressed such that repeated sequences are shortened by a number.

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
    i = len(compressed) - 1

    while i >= 0:
        skip = 1
        character = compressed[i]

        if character == "[":
            i -= skip
            continue

        if not character.isdigit():
            character_stack.append(character)
        else:
            # Look ahead to see if the next character is apart of this numerical value
            j = i - 1 
            extra_digits = [compressed[i]]
            while compressed[j].isdigit():
                extra_digits.append(compressed[j])
                j -= 1
            repeat = int("".join(reversed(extra_digits)))
            skip = len(extra_digits)

            # Form the current substring and repeat it by the numerical value
            sub_string = []
            while character_stack[-1] != "]":
                sub_string.append(character_stack.pop())
            character_stack.pop()

            character_stack.append(repeat * "".join(sub_string))
        i -= skip

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
    
    def test_nested(self):
        self.assertEqual(decompress_str("2[3[a]]"), "aaaaaa")
        self.assertEqual(decompress_str("2[2[b]3[a]]"), "bbaaabbaaa")
        self.assertEqual(decompress_str("2[2[b]3[a]cd]"), "bbaaacdbbaaacd")
        self.assertEqual(decompress_str("3[c4[a2[b]]]"), "cabbabbabbabbcabbabbabbabbcabbabbabbabb")

    def test_multiple_digits(self):
        self.assertEqual(decompress_str("10[a]"), 10*"a")
        self.assertEqual(decompress_str("123[a]"), 123*"a")

if __name__ == "__main__":
    unittest.main()