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

        index = self._hash_mod(key)

        # self.storage[index] = value

        node = self.storage[index] 

        if node is None:
            self.storage[index] = LinkedPair(key, value)
            return

        while node.next is not None:
            node = node.next
        
        node.next = LinkedPair(key, value)

        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        pass



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # index = self._hash_mod(key)

        # node = self.storage[index]

        # if node is None:
        #     print("This key is not found!")
        #     return

        # # if node.key == key:
        # #     if node.next: 
        # #         node = node.next
        # #     else:
        # #         node = None

        # while node is not None and node.key != key:
        #     node = node.next
        
        # node = None
        # # if node.key == key:
        # #     if node.next: 
        # #         node = node.next
        # #     else:
        # #         node = None
        index = self._hash_mod(key)

        current_node = self.storage[index]

        if current_node is None:
            print("This key is not found!")
            return
        else:
            if current_node.key == key or current_node.next is None:
                self.storage[index] = current_node.next
                return
            else:
                while current_node is not None:
                    next_node = current_node.next

                    if next_node.key == key:
                      current_node.next = next_node.next
                      return
                    current_node = current_node.next


        # index = self._hash_mod(key)
        # # check to see if the value at the index is not None
        # if self.storage[index] is not None:
        #     # set the current pair to the head of the linked list
        #     current_pair = self.storage[index]
        #     # if current pair key == key or there is no next pair, set the current index to current_pair next
        #     if current_pair.key == key or current_pair.next is None:
        #         self.storage[index] = current_pair.next
        #         # decrement the count
        #         # self.items -= 1
        #         return 
        #     # otherwise
        #     else:
        #         # loop through the linked list
        #         while current_pair is not None:
        #             # let next pair = current pair next
        #             next_pair = current_pair.next
        #             # if next pair key == key
        #             if next_pair.key == key:
        #                 # set current pair next to next pair next
        #                 current_pair.next = next_pair.next
        #                 # decrement the count
        #                 # self.items -= 1
        #                 return 
        #             # set current pair to current pair next
        #             current_pair = current_pair.next
        # # otherwise, print a warning
        # else:
        #     print("No match for that key!")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        node = self.storage[index]

        if node is None:
            return None

        while node is not None and node.key != key:
            node = node.next
            
        return node.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        pass



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
