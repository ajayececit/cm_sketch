import string
import random
from probables import CountMinSketch
import time
import sys

# Generate a large input of random characters
input_size = 10**3
input_data = ''.join(random.choice(string.ascii_lowercase) for _ in range(input_size))

# Hash Table
hash_table = {}
for char in input_data:
    if char in hash_table:
        hash_table[char] += 1
    else:
        hash_table[char] = 1
hash_table_space = sys.getsizeof(hash_table)

# CM Sketch
cm_sketch = CountMinSketch(4, 1000)
cms_start_time = time.time()
for char in input_data:
    cm_sketch.add(char)

# cms_space = cm_sketch.memory_usage()
cms_space = sys.getsizeof(cm_sketch)

# Print the results
print("CM Sketch vs Hash Table Memory Utilization")
print("Hash Table:")
print("Space: {} bytes".format(hash_table_space))
print()
print("CM Sketch:")
print("Space: {} bytes".format(cms_space))
percentage_difference = ((hash_table_space - cms_space) / hash_table_space) * 100
print("Percentage Difference: {} %".format(percentage_difference))


