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
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        address = self._hash_mod(key)
        
        node = LinkedPair(key, value)
        node.next = self.storage[address]
        self.storage[address] = node



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        address = self._hash_mod(key)
        if not self.storage[address]:
            print('Warning! There is no key that you are looking for!')
        
        # self.storage[address] = self.storage[address].next

        node = self.storage[address]

        if node.key == key:
            self.storage[address] = node.next
        

        arr = []
        while node is not None:
            if node.key != key:
                arr.append(node)
            node = node.next

        for i in range(0, len(arr)-1):
            if arr[i + 1] is not None:
                arr[i].next = arr[i+1]

        if len(arr) > 0:
            self.storage[address] = arr[0]
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        address = self._hash_mod(key)
        if not self.storage[address]:
            # print('1', self.storage[address].__dict__)
            return None
        node = self.storage[address]
        # print('2', self.storage[address].__dict__)
        while node is not None:
            curr = node
            node = curr.next
            if curr.key == key:
                return curr.value


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        old = self.storage
        self.storage = [None] * self.capacity

        for i in old:
            while i is not None:
                self.insert(i.key, i.value)
                i = i.next


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