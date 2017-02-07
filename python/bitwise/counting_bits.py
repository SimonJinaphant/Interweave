def counting_bits(num):

    result = [0] * (num+1)

    for i in xrange(1, num+1):
        result[i] = result[i >> 1] + (i & 1)

    return result

print counting_bits(5)
print counting_bits(10)
print counting_bits(15)