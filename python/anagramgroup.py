from __future__ import absolute_import
import unittest


def anagram_group(words):
    """Given a list of words, group anagrams of the same word together into a list

    :param words: A list of lowercase words from the english alphabet
    :return: A collection of lists of words each containing the same anagrams
    """

    '''
    Anagrams have the same hash value so we'll place words with the same hash into the same bucket
    Prime numbers are good for generating hashes since the product of a prime with any other number has the good chance
    of being unique.
    '''

    buckets = {}
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]

    for word in words:

        # Calculate the hash for this certain word.
        hash_key = 1
        for letter in word:
            hash_key *= primes[ord(letter) - ord("a")]

        # Add the hash to a certain bucket or create a new one if needed.
        if hash_key in buckets:
            buckets[hash_key].append(word)
        else:
            buckets[hash_key] = [word]

    return buckets.values()


class AnagramGroupTest(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(anagram_group(["tea", "eat", "ate", "tan", "bat", "nat"]), [['tan', 'nat'], ['tea', 'eat', 'ate'], ['bat']] )