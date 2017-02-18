def max_sum_non_adj(numbers):
    inclusive = numbers[0]
    exclusive = 0

    for i in xrange(1, len(numbers)):
        temp = inclusive

        inclusive = max(exclusive+numbers[i], inclusive)
        exclusive = temp

    return inclusive


print max_sum_non_adj([4, 1, 1, 4, 2, 1])