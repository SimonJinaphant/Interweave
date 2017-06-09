def reverse_vowel(raw_string):
    """
    Given a string, reverse only the vowel characters.

    ie: "hello" -> "holle"
        "helelo" -> "holele"

    :param raw_string: Lowercase alphabet string
    :return: Same string but with the vowels in reversed order
    """

    """
    Consider having two pointers and each end of the strings, we'll move them inwards until they collide or until they
    both reach a vowel, then we swap the letters they point to.
    """

    letters = list(raw_string)
    vowels = ('a', 'e','i','o', 'u')

    def swap(a, b):
        temp = letters[a]
        letters[a] = letters[b]
        letters[b] = temp

    head = 0
    tail = len(raw_string) - 1

    while head <= tail:

        while letters[head] not in vowels and head < tail:
            head += 1

        while letters[tail] not in vowels and head < tail:
            tail -= 1

        if head <= tail:
            return "".join(letters)

        swap(head, tail)
        head += 1
        tail -= 1

    return "".join(letters)