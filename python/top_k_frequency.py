def top_k_frequency(data, k):
    occurrences = {}
    max_occurrence = 1
    for d in data:
        if d in occurrences:
            occurrences[d] += 1
            max_occurrence = max(max_occurrence, occurrences[d])
        else:
            occurrences[d] = 1

    buckets = [[] for i in xrange(max_occurrence)]
    for data_key, data_occurrence in occurrences.iteritems():
        buckets[data_occurrence - 1].append(data_key)

    result = []
    for bucket in buckets[k-1:]:
        result.extend(bucket)

    return result

print top_k_frequency([1,1,1,2,2,3], 2)
