def subarray_sum_to_target(numbers, target):
    start = 0
    end = 1
    sum = numbers[start]

    while end != len(numbers):
        if sum < target:
            sum += numbers[end]
            end += 1
        elif sum > target:
            sum -= numbers[start]
            start += 1
        else:
            return numbers[start: end]

    return None

print subarray_sum_to_target([1,4,20,3,10,5], 33)
print subarray_sum_to_target([1,4,0,0,3,10,5], 7)
print subarray_sum_to_target([1,4], 0)