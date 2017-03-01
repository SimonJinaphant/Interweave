# Project Interweave
Combining the theories and practices of modern day Computer Science


# Arrays

### Searching
...

### Target Summation
You need to find N distinct numbers from a single array, OR find one number each from N arrays, which sums up to a target value.

The brute-force way is to use N loops to arbitrarily choose a number and check if those number combinations make the sum; but we can do better.

When we've arbitrarily chosen N-1 numbers, we can calculate the last number we need to obtain the target sum; thus we can optimize by searching for that number.
```
a + b + c + ... + z = target
z = target - (a + b + c + ... + n-1)    (re-arrange sides)
```

- If the array(s) are sorted we can utilize binary search to find the last number we need to make our target sum.
  - Alternatively, when dealing with a single sorted array and searching for only 2 elements we can [have pointers at each end](python/sums_of_two.py) and move them inwards until we have the sum.

```python
for i in xrange(len(arr_a)):
  for j in xrange(len(arr_b)):
    ...
    if BinarySearch(arr_n, target - (arr_a[i]+arr_b[j])):
      return True
```
See: [sums_of_two.py](python/sums_of_two.py)

- If the array(s) are unsorted we use a Set to remember the last number to find: every iteration we check if the current number is one of numbers we needed previously, otherwise we calculate what number we'll need to make the current numbers sum to the target.

```python
for i in xrange(0, len(numbers)-2):

       record = set([])

       for j in xrange(i+1,len(numbers)):

           if numbers[j] not in record:
               record.add(target-(numbers[i]+numbers[j]))
           else:
               return True

   return False
```
See: [sums_of_three.py](python/sums_of_three.py)

### Contiguous subarrays
...

### Sub-sequences
...

# Strings
### Sub-strings
Bruteforce vs Boyer Moore vs Rabin Karp

### Anagrams and Hashes

### Occurrences and Bucket Sorting

### Tries

# Sorting and Partition

# Binary Trees
### Serialize and Deserialize

# Graphs
### Level Order Traversal

# Bitwise
### Multiply and Exponent
### The importance of LSB
- Finding min/max
### Binary Sequences
- Finding a missing number

# Dynamic Programming
