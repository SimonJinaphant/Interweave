# Project Interweave
Combining the theories and practices of modern day Computer Science


# Arrays

### Searching
...

### Target Summation
You need to find N distinct numbers from a single array -OR find a single number from each of the N arrays- which sums up to a target value.

The brute-force way is to use N loops to arbitrarily choose a number amd check if those selected number make the sum; but we can do better.

When we've arbitrarily chosen N-1 numbers, we can calculate the last number we need to obtain the target sum; thus we can optimize by searching for that number.
```
n_1 + n_2 + n_3 + ... + n_(n-1) = target
z = target - (n_1 + n_2 + n_3 + n_(n-1) )    (re-arrange sides)
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

- If the array(s) are unsorted we use a Set to remember the last number to find: every iteration in the most nested loop we check if the current number is one of numbers we needed previously, otherwise we calculate what number we'll need to make the current numbers sum to the target.

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
Bruteforce vs [Boyer Moore](python/boyer_moore.py) vs [Rabin Karp](python/rabin_karp.py)

- Boyer Moore:
Smarter comparision by using a bad character rule to skip many unnecessary comparisons.

- Rabin Karp:
Utilize string hashing to match sub-strings; can be utilzed to compare multiple strings at a time.

### Anagrams and Hashes

Anagrams are simply words with characters rearranged, therefore they:
 - Have the *exact* same amount of characters
 - Look the *exact* same when sorted by their characters
 - Have the same hash value

When hashing consider the usage of prime numbers; the product of a prime number with another number has a higher chance of being unique

See: [anagramgroup.py](python/anagramgroup.py)

### Occurrences and Bucket Sorting

When dealing with occurrences, we can use a dictionary or a fixed length set if the radix is known.

When grouping similar occurrences together (in order to find top K occurences) consider dumping the contents of the above collections into buckets based on their occurrences.

See: [top_k_occurrence](python/top_k_occurrence), [sort_by_occurrence](python/sort_by_occurrence)

### Tries

A Trie is a ordered tree for strings based on their prefixes.
 - All descendants of a Trie node share the same prefix.
 - Leaf nodes are always completed words, but intermediates can be either.

See: [autocomplete.py](python/autocomplete.py)

### Parsing by Replacing

Given some string, we need to modify it such that the result string has some characters replaced with another
 - Consider working backwards (from right to left) to avoid having to shift the string every time we add a new character but there's still letters to the right of it.

See: [decompress_str.py](python/decompress_str.py)

# Sorting and Partition

# Binary Trees
### Serialize and Deserialize

# Graphs
### Level Order Traversal
Breadth first traversal doesn't explicitly indicate when we reach a new depth level in the binary tree; however we can fix this by keeping track of two counters: one for the current level, and another for the next level.
- When we dequeue a node out of the queue we decrement the current level by 1.
- When we enqueue a node into the queue we increment the next level counter by 1.
- Once current level reaches 0 we know we've finished a traversing all nodes in a particular level.
- Simply swap the counter values and do the same thing all over again to start traversing the next level.

See [max_tree_row](python/max_tree_row.py)

# Bitwise
### Multiply and Exponent
- The left and right shift operator is the same as multiplying or dividing the numerical value by 2;
this is helpful as it can express multiplication as sums of powers of 2:
  - The expression `3 * 4` is the same as `3 * 2^2` which is the same as `3 * (1 << 2)`

- When you want to check if a certain bit in a binary is a 0 or a 1 use the shift operator and the AND operator
`(binary >> bit_position) & 1`

- When you want to set a certain bit in a binary to a 1, use the OR operator
`binary |= (1 << bit_position)`

- Toggling a certain bit can be done with the XOR operator
`binary ^= (1 << bit_position)`

- An alternative way of flipping a single bit is `1 ^ bit`

- To obtain an n-length binary of all 1's we can do `(1 << (n+1)) - 1)`

### The importance of LSB
- If a number is odd it has a 1 for its LSB
- If a number is even it has a 0 for its LSB

See Finding min/max

### Binary Sequences

- Finding a missing number

# Dynamic Programming
