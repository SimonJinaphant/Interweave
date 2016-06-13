def anagram_group(words):

    record = {}
    for word in words:
        sum = 0
        for letter in word:
            sum += ord(letter)-ord('a')

        if sum in record:
            record[sum].append(word)
        else:
            record[sum] = [word]

    result = []
    for group in record.itervalues():
        result.append(group)

    return result

print anagram_group(["tea", "eat", "ate", "tan", "bat", "nat"])