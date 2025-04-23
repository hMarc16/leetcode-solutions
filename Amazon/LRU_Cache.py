class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:
    # Double LinkedList + Hash Map

    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}   # Hash map mapping key to node

        # For most recent and least recent vals
        # left is the LRU, right is the MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # Rm any node from the LL
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # Insert to the rightmost pos
    def insert(self, node):
        # Because insert to the rightmost
        prev, nxt = self.right.prev, self.right
        # Both pointing at node
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.map:
            # remove it from its prev pos
            self.remove(self.map[key])
            # Then insert it to the rightmost pos
            self.insert(self.map[key])
            # Return the value
            return self.map[key].val    # This tells the node, then get val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # If key is already in cache, node is already existing in the LL
        if key in self.map:
            # Remove the old node so that a new val can be assigned to that key
            self.remove(self.map[key])
        self.map[key] = Node(key, value)
        # After creating the node, insert it into the double LL
        self.insert(self.map[key])

        if len(self.map) > self.cap:
            # rm the LRU from the LL and the map
            lru = self.left.next
            # rm from LL
            self.remove(lru)
            # Delete from the map
            del self.map[lru.key]
