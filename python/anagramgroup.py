import unittest


def anagram_group(words):
    """Given a list of words, group anagrams of the same word together into a list

    :param words: A list of words
    :return: A collection of lists each containing the same anagrams
    """
    record = {}
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

    for word in words:
        hash_key = 1
        for letter in word:
            hash_key *= primes[ord(letter) - ord("a")]

        if hash_key in record:
            record[hash_key].append(word)
        else:
            record[hash_key] = [word]

    result = []
    for group in record.itervalues():
        result.append(group)

    return result


class AnagramGroupTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(anagram_group(["tea", "eat", "ate", "tan", "bat", "nat"]), [['tan', 'nat'], ['tea', 'eat', 'ate'], ['bat']] )