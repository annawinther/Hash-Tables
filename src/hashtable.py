# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.count = 0
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

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # if self.count >= self.capacity:
        #     self.resize()
        #     return
        
        index = self._hash_mod(key)

        current_node = self.storage[index] 

        if current_node is None:
            self.storage[index] = LinkedPair(key, value)
            return
        else:
            # loop through the items at that index until we find the end (self.next is none)
            while current_node.key != key:
                if current_node.next is None:
                    current_node.next = LinkedPair(key, value)
                    return
                else:
                    current_node = current_node.next
        current_node.value = value


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # #compute index of key using a hash function 
        # index = self._hash_mod(key)
        # node = self.storage[index]
        # prev = None
        # #iterate to the requested node 
        # while node is not None and node.key != key: 
        #   prev = node
        #   node = node.next 
        # if node is None:
        #   print("warning! key is not found")
        # else: 
        #   self.count -= 1 
        #   result = node.value
        #   if prev is None:
        #     self.storage[index]  = node.next 
        #   else: 
        #     prev.next = prev.next.next
        #   return result
        
        index = self._hash_mod(key)

        current_node = self.storage[index]

        if current_node is None:
            print("This key is not found!")

        else:
            if current_node.key == key or current_node.next is None:
                self.storage[index] = current_node.next

            else:
                while current_node is not None:
                    next_node = current_node.next

                    if next_node.key == key:
                      current_node.next = next_node.next

                    current_node = current_node.next



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        current_node = self.storage[index]

        if current_node is None:
            return None

        while current_node and current_node.key != key:
            current_node = current_node.next
            
        return current_node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # if self.count >= self.capacity:
        self.capacity *= 2
        store = self.storage
        self.storage = [None] * self.capacity

        for i in store:
            node = i
            if node:
                current = node
                while current is not None:
                    self.insert(current.key, current.value)
                    current = current.next



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

    print("")
