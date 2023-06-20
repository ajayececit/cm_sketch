from pyprobables import CountMinSketch

# Create a Count-Min Sketch with 4 hash functions and a width of 1000
cms = CountMinSketch(4, 1000)

# Data stream: [A, B, K, A, A, K, S]
data_stream = ['A', 'B', 'K', 'A', 'A', 'K', 'S']

# Process the data stream and update the Count-Min Sketch
for item in data_stream:
    cms.add(item)

# Query the Count-Min Sketch to get the estimated counts
print("Estimated counts:")
print(f"A: {cms.check('A')}")
print(f"B: {cms.check('B')}")
print(f"K: {cms.check('K')}")
print(f"S: {cms.check('S')}")
