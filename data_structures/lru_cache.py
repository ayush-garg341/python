"""
Implementing LRU cache in python.
Least recently used.
"""

from datetime import datetime


class Node:
    def __init__(self, data):
        self.data = data
        self.time = None
        self.next = None


class LRUCache:
    def __init__(self):
        self.head = None
        self.size = 5
        self.num_elts = 0
        self.hash_map = dict()

    def insert(self, key, value):
        if self.hash_map.get(key, None):
            self.update_existing_key(key)
        else:
            if self.num_elts != self.size:
                self.hash_map[key] = value
                self.add_to_linked_list(key)
                self.num_elts += 1
            else:
                key_to_be_removed = self.evict_least_recently_used_key()
                self.num_elts -= 1
                del self.hash_map[key_to_be_removed]
                self.hash_map[key] = value
                self.add_to_linked_list(key)
                self.num_elts += 1

    def get(self, key):
        if self.hash_map.get(key, None):
            self.update_existing_key(key)
            return self.hash_map.get(key)
        else:
            raise Exception("Key not found")

    def update_existing_key(self, key):
        temp_node = self.head
        prev_node = None
        while temp_node.data != key:
            prev_node = temp_node
            temp_node = temp_node.next
        prev_node.next = temp_node.next

        self.add_to_linked_list(key)

    def add_to_linked_list(self, key):
        node = Node(key)
        node.next = self.head
        node.time = datetime.now()
        self.head = node

    def evict_least_recently_used_key(self):
        temp_node = self.head
        prev_node = None
        while temp_node.next != None:
            prev_node = temp_node
            temp_node = temp_node.next
        prev_node.next = None
        key = temp_node.data
        return key

    def print_all_keys_linked_list(self):
        temp_node = self.head
        while temp_node != None:
            print("{},{}".format(temp_node.data, temp_node.time), end=" ---> ")
            temp_node = temp_node.next


lru = LRUCache()
lru.insert("5", 5)
lru.insert("4", 4)
lru.insert("3", 3)
lru.insert("2", 2)
lru.insert("1", 1)

lru.print_all_keys_linked_list()

lru.insert("10", 10)
print("\n")


print(lru.get("3"))
lru.print_all_keys_linked_list()
