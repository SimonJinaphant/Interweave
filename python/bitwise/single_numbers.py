def single_numbers(numbers):
    xor_result = 0
    for num in numbers:
        xor_result ^= num

    interesting_bit = 1
    while xor_result & interesting_bit == 0:
        interesting_bit <<= 1

    first_single = 0
    second_single = 0
    for num in numbers:
        if num & interesting_bit == 0:
            first_single ^= num
        else:
            second_single ^= num

    return (first_single, second_single)

print single_numbers([1,2,1,3,2,5])