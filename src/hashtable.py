# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    # def __repr__(self):
    #     return f"<{self.key}, {self.value}>"

class HashTable:
    '''
    A hash table with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        
        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        target = False
        if self.storage[index] is not None:
            while current_node and not target:
                if current_node:
                    current_node.value = value
                    target = True
                elif current_node.next == None:
                    current_node.next = LinkedPair(key, value)
                    print(current_node.next)

        self.storage[index] = LinkedPair(key, value)
    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index]:
            self.storage[index] = None
        else: 
            print("key not found")
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index] is None:
            return None
        else:
            return self.storage[index]
        


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        for pair in old_storage:
            if pair is not None:
                new_index = self._hash_mod(pair.key)
                self.storage[new_index] = LinkedPair(pair.key, pair.value)
        self.storage[new_index]       


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))
    



# import time
# import bcrypt
# ​
# input_string = b"apple"
# n = 1000000
# ​
# print(f"Hashing {n}x")
# ​
# start_time = time.time()
# for i in range(n):
#     output_hash = hash(input_string)
# end_time = time.time()
# print (f"  Python hash runtime: {end_time - start_time} seconds")
# ​
# def djb2(key):
#     '''
#     DJB2 hash
#     '''
#     # Start from an arbitrary large prime
#     hash_value = 5381
#     # Bit-shift and sum value for each character
#     for char in key:
#         hash_value = ((hash_value << 5) + hash_value) + char
#     return hash_value
# ​
# ​
# ​
# start_time = time.time()
# for i in range(n):
#     djb2(input_string)
# end_time = time.time()
# print(djb2(input_string))
# print(f"  DJB2 hash runtime: {end_time - start_time} seconds")
# ​
# ​
# ​
# start_time = time.time()
# salt = bcrypt.gensalt()
# for i in range(5):
#     bcrypt.hashpw(input_string, salt)
# end_time = time.time()
# print(f"  bcrypt hash runtime: {end_time - start_time} seconds")