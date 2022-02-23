from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        value = 0
        for i in word:
            value += ord(i)
        return value % len(self.buckets)

    # Doubles size of bucket list
    def rehash(self):
        l1 = self.buckets

        # Creates a new empty list twice the size
        self.buckets = [[] for x in range(0, len(self.buckets) * 2)]
        self.size = 0
        for i in l1:
            for word in i:
                self.add(word)

    # Adds a word to set if not already added
    def add(self, word):
        value = self.get_hash(word)
        if self.contains(word) is False:
            if self.size == len(self.buckets):
                self.rehash()
                self.add(word)
            else:
                self.buckets[value].append(word)
                self.size += 1

    # Returns a string representation of the set content
    def to_string(self):
        string = "{ "
        for i in self.buckets:
            for j in i:
                string += f"{j} "
        string += "}"
        return string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        return word in self.buckets[self.get_hash(word)]

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing if word not in set
    def remove(self, word):
        if self.contains(word) is True:
            self.buckets[self.get_hash(word)].remove(word)
            self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        max = 0
        for i in range(len(self.buckets)):
            if len(self.buckets[i]) > max:
                max = len(self.buckets[i])
        return max
