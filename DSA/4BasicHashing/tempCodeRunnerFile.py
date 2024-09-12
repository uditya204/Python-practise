class MyHash:
    def __init__(self, n):
        self.bucket_size = n
        self.hash_table = [[] for _ in range(self.bucket_size)]
    
    def insert(self, value):
        hash_value = value %  self.bucket_size
        self.hash_table[hash_value].append(value)
    
    def search(self, key):
        hash_value = key %  self.bucket_size
        if key in self.hash_table[hash_value]:
            return True
        else:
            False

    def remove(self, key):
        hash_value = key %  self.bucket_size
        self.hash_table[hash_value].remove(key)


"""

BUCKET = 7
So, HASH_FUNCTION = x % BUCKET = x % 7

"""
h = MyHash(7)

h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.hash_table)

print(h.search(56))       #Output:- True

h.remove(56)
print(h.hash_table)

print(h.search(56))       #Output:- False