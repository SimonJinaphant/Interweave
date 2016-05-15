def magic_index(numbers):
    lower_bound = 0
    upper_bound = len(numbers) -1

    while lower_bound <= upper_bound:
        mid = (upper_bound + lower_bound) / 2

        if numbers[mid] == mid:
            return mid
        elif numbers[mid] > mid:
            upper_bound = mid - 1
        else:
            lower_bound = mid + 1

    return None

print magic_index([-40, -20, -1, 1, 2, 3, 5, 6, 7, 9, 12, 13])
print magic_index([-40, -20, 1, 3, 5, 6, 7, 9, 13])