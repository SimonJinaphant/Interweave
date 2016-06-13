def anagram_group(words):
    """Given a list of words, group anagrams of the same word together into a list
    :param words: A list of words
    :return: A collection of lists each containing the same anagrams
    """
    record = {}

    for word in words:
        sum = 0
        for index, letter in enumerate(word):
            sum += ord(letter) - ord('a')

        if sum in record:
            record[sum].append(word)
        else:
            record[sum] = [word]

    result = []
    for group in record.itervalues():
        result.append(group)

    return result

print anagram_group(["tea", "eat", "ate", "tan", "bat", "nat"])