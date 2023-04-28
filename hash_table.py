import csv
import hashlib
import pandas as pd
import openpyxl

# Hash table data structure implementation.
class HashTable:

    # Hash Table size starts with 8
    MIN_SIZE = 8

    # Consturctor
    def __init__(self, hashing_function='division'):
        self.ID = 0
        self._size = self.MIN_SIZE
        self._slots = [[] for _ in range(self._size)]
        self._hashing_function = hashing_function
        self._len = 0

    # hash the key inserted with two steps:
    # 1. If the key is a string, the function adds up the ASCII values of its characters to generate a sum.
    # 2. The function then applies the key hashing to obtain an index within the range of available slots in the table.
    def _hash(self, key):

        key = sum(ord(c) for c in key) if type(key) is str else key
        return {
            'division': lambda: key % self._size
        }.get(self._hashing_function, lambda: None)()

    #retrieves the value associated with a specified key,
    # but if the key does not exist, it returns a default value.
    # If no default value is specified, it returns None.
    def get(self, key, default=None):

        index = self._hash(key)
        slot = self._slots[index]
        for pair in slot:
            if pair[0] == key:
                return pair[1]
        return default

    #  Check if key already exists inside the hash table.
    def exist(self, key):

        index = self._hash(key)
        slot = self._slots[index]
        return key in dict(slot)

    # adds a pair of a key and its corresponding value to the hash table.
    # Collisions are handled using a chaining approach, and therefore, not taken into account.
    # It is not possible to add a key that already exists in the hash table.
    def put(self, key, value):
        if not self.exist(key):
            index = self._hash(key)
            self._slots[index].append((key, value))
            self._len += 1
            if self._len > self._size:
                self._expand()

    # deletes a key and its corresponding value from the hash table, and returns the value.
    # If the specified key is not found, it returns a default value.
    # If no default value is specified, it returns None.
    def remove(self, key, default=None):
        index = self._hash(key)
        slot = self._slots[index]
        pop_index = None
        for i in range(len(slot)):
            if slot[i][0] == key: pop_index = i
        if pop_index is not None:
            removed_pair = slot.pop(pop_index)
            self._len -= 1
            if self._len == self._size / 4 and self._size > self.MIN_SIZE:
                self._shrink()
            return removed_pair
        else:
            return default

    # increases the capacity of the hash table by adding more slots
    # and performs a rehashing of all (key, value) pairs to fit the new size of the table.
    # It is used when the number of key entries exceeds the number of slots available in the hash table.
    def _expand(self):
        temp_slots = []
        for slot in self._slots:
            temp_slots += slot

        self._size *= 2
        self._len = 0
        self._slots = [[] for _ in range(self._size)]

        for pair in temp_slots:
            self.put(pair[0], pair[1])

    #reduces the capacity of the hash table by removing some slots
    # and performs a rehashing of all (key, value) pairs to fit the new size of the table.
    # It is used when the number of key entries is equal to one-fourth of the number of slots available in the hash table.
    def _shrink(self):
        temp_slots = []
        for slot in self._slots:
            temp_slots += slot

        self._size //= 2
        self._len = 0
        self._slots = [[] for _ in range(self._size)]

        for pair in temp_slots:
            self.put(pair[0], pair[1])









