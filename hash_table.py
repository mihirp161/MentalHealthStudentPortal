import csv
import hashlib

class HashTable:
    """
    Hash table data structure implementation.
    This implementation uses chaining for collision resolution.
    This data structure basically receives a pair (key, value)
    and add it to the hash tabel structure.
    """
    MIN_SIZE = 8

    def __init__(self, hashing_function='division'):
        self._size = self.MIN_SIZE
        self._slots = [[] for _ in range(self._size)]
        self._hashing_function = hashing_function
        self._len = 0

    # def _hash(self, key):
    #     """
    #     Applies SHA256 hashing process to a given key and return an index
    #     from the table slots.
    #     """
    #     if isinstance(key, str):
    #         key = key.encode('utf-8')
    #     hash_value = int.from_bytes(hashlib.sha256(key).digest(), byteorder='big')
    #     return hash_value % self._size

    def _hash(self, key):
        """
        Applies hashing process to a given key and return an index
        from the table slots. This is done in two steps :
        1. Checks if the key is a string and returns the equivalent
        sum of its ASCII values.
        2. Applies the key hashing to an index in the slots range
        """
        key = sum(ord(c) for c in key) if type(key) is str else key
        return {
            'division': lambda: key % self._size
        }.get(self._hashing_function, lambda: None)()
        # if isinstance(key, str):
        #     key = key.encode('utf-8')
        # hash_value = int.from_bytes(hashlib.sha256(key).digest(), byteorder='big')
        # return hash_value % self._size



    # def get(self, key, default=None):
    #     """
    #     Returns the value for given key if the key exists,
    #     else returns default value.
    #     Default value is None if not specified.
    #     """
    #     index = self._hash(key)
    #     slot = self._slots[index]
    #     for pair in slot:
    #         return pair[1] if pair[0] == key else default

    def get(self, key, default=None):
        """
        Returns the value for given key if the key exists,
        else returns default value.
        Default value is None if not specified.
        """
        index = self._hash(key)
        slot = self._slots[index]
        for pair in slot:
            if pair[0] == key:
                return pair[1]
        return default

    def exist(self, key):
        """
        Check if key already exists inside the hash table.
        """
        index = self._hash(key)
        slot = self._slots[index]
        return key in dict(slot)

    # def put(self, key, value):
    #     """
    #     Inserts a key and value pair inside the hash table.
    #     The collisions are resolved using separate chaining.
    #     Repeated keys cannot be added.
    #     """
    #     index = self._hash(key)
    #     slot = self._slots[index]
    #     for pair in slot:
    #         if pair[0] == key:
    #             pair[1] = value
    #             return  # update value if key already exists
    #     slot.append((key, value))  # add new (key, value) pair to list
    #     self._len += 1
    #     if self._len > self._size:
    #         self._expand()

    def put(self, key, value):
        """
        Inserts a key and value pair inside the hash table.
        The collisions are ignored as a chaining approach is taken.
        Repeated keys can not be added.
        """
        if not self.exist(key):
            index = self._hash(key)
            self._slots[index].append((key,value))
            self._len += 1
            if self._len > self._size:
                self._expand()

    def remove(self, key, default=None):
        """
        Removes and returns a given key value and its associated value pair.
        If given key is not found, the given default value is returned.
        If default value is not provided, None is returned.
        """
        index = self._hash(key)
        slot = self._slots[index]
        pop_index = None
        for i in range(len(slot)):
            if slot[i][0] == key: pop_index = i
        if pop_index is not None:
            removed_pair = slot.pop(pop_index)
            self._len -= 1
            # If the amount of entries is 1/4 of the total amount of slots and
            # the total amount of slots is greater then the minimun size, than
            # a shirnking is applied ot the hash table
            if self._len == self._size/4 and self._size > self.MIN_SIZE:
                self._shrink()
            return removed_pair
        else:
            return default

    def _expand(self):
        """
        Expands the slots capacity from the hash table, applying a
        rehash on all (key, value) pairs to match the new size of the
        hash table.
        Applied when number of key entries is bigger than the amount of slots.
        """
        temp_slots = []
        for slot in self._slots:
            temp_slots += slot

        self._size *= 2
        self._len = 0
        self._slots = [[] for _ in range(self._size)]

        for pair in temp_slots:
            self.put(pair[0], pair[1])

    def _shrink(self):
        """
        Shrinks the slots capacity from the hash table, applying a
        rehash on all (key, value) pairs to match the new size of the
        hash table.
        Applied when number of key entries is 1/4 of the amount of slots.
        """
        temp_slots = []
        for slot in self._slots:
            temp_slots += slot

        self._size //= 2
        self._len = 0
        self._slots = [[] for _ in range(self._size)]

        for pair in temp_slots:
            self.put(pair[0], pair[1])


if __name__ == "__main__":
    #main()
    h = HashTable()

    # h.put(1, "test")
    # print(h.get(1))

    # print(h._hash("test"))
    # print(h.get("8"))
    # print(h.put("test","test"))
    # print(h.get("8"))


    with open('fake_dataframe_testSubset.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for idx, row in enumerate(csv_reader):
            # h.put(row[4], row)
            print(f'{idx}: {h._hash(row[4])}')
            h.put(row[4], row)

    with open('fake_dataframe_testSubset.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for idx, row in enumerate(csv_reader):
            print(row[4])
            print(f'{idx}: {h.get(row[4])}')



