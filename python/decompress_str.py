def decompress_str(compressed):
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

    final_str = []
    while len(character_stack) != 0:
        final_str.append(character_stack.pop())

    return "".join(final_str)

print decompress_str("3[a2[c]]")
print decompress_str("3[a]2[bc]")