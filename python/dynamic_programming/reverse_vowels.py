def reverse_vowel(raw_string):
    buffer = list(raw_string)
    vowels = ('a', 'e','i','o', 'u')

    def swap(a, b):
        temp = buffer[a]
        buffer[a] = buffer[b]
        buffer[b] = temp

    head = 0
    tail = len(raw_string) - 1

    while head <= tail:

        while buffer[head] not in vowels and head < tail:
            head += 1

        while buffer[tail] not in vowels and head < tail:
            tail -= 1

        if head <= tail:
            return "".join(buffer)

        swap(head, tail)
        head += 1
        tail -= 1

    return "".join(buffer)