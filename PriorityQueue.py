"""
Authors: Tung Tran & Jake Etzler
"""

from heapq import *


class PriorityQueue(object):
    def __init__(self, is_greater_func=None):
        """
        Priority Queue abstract class. Inherit from this class!
        
        Arguments:
        is_greater_func: (Optional) Function to compare datatypes 
                    used in algorithm. E.g: A function to compare 
                    nodes could be:
                    def is_greater_node(node1, node2):
                        return node1.val > node2.val
        """
        self.is_greater_func = is_greater_func if is_greater_func \
                                            else lambda x, y: x > y
    
    def __str__(self):
        """ Prints out the priority queue for debugging purposes. """
        pass
    
    def isEmpty(self):
        pass
    
    def push(self, data):
        """ Inserts `data` of appropriate type (must be comparable  
            using `self.is_greater_func`)"""
        pass
    
    def pop(self):
        """ Deletes a `data` instance and return it. """
        pass
    
    
class PQBinaryHeap(PriorityQueue):
    def __init__(self, is_greater_func=None):
        """
        Priority Queue implemented with Binary Heap. 
        
        Arguments:
        is_greater_func: (Optional) Function to compare datatypes 
                    used in algorithm. E.g: A function to compare 
                    nodes could be:
                    def is_greater_node(node1, node2):
                        return node1.val > node2.val
        """
        super().__init__(is_greater_func=is_greater_func)
        self.heap = []
        self.tail = -1
    
    def __str__(self):
        """ Prints out the priority queue for debugging purposes. """
        return str(self.heap)
    
    def isEmpty(self):
        return len(self.heap) == 0
    
    def push(self, data):
        """ Inserts `data` of appropriate type (must be comparable  
            using `self.is_greater_func`)"""
        self.tail += 1
        if len(self.heap) == self.tail:
            self.heap.append(data)
        else:
            self.heap[self.tail] = data
        self.shift_up()
    
    def pop(self):
        """ Deletes a `data` instance and return it. """
        if self.tail == -1:
            return None
        ret = self.heap[0]
        self.heap[0] = self.heap[self.tail]
        self.tail -= 1
        self.shift_down(0)
        return ret
    
    def shift_up(self):
        i = self.tail 
        while i > 0 and self.is_greater_func(self.heap[i], self.heap[self.parent(i)]):
            self.heap[self.parent(i)], self.heap[i] = \
                    self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
    
    def shift_down(self, i):
        idx = i
        idx_left = i*2 + 1
        idx_right = i*2 + 2
        if idx_left <= self.tail and \
                self.is_greater_func(self.heap[idx_left], self.heap[idx]):
            idx = idx_left
        if idx_right <= self.tail and \
                self.is_greater_func(self.heap[idx_right], self.heap[idx]):
            idx = idx_right
        if i != idx:
            self.heap[i], self.heap[idx] = \
                    self.heap[idx], self.heap[i]
            self.shift_down(idx)
            
    def parent(self, i):
        return (i-1) // 2
    

class PQDummy(object):
    def __init__(self, is_greater_func=None):
        """
        A simple Priority Queue for testing & benchmarking.
        
        Arguments:
        is_greater_func: (Optional) Function to compare datatypes 
                    used in algorithm. E.g: A function to compare 
                    nodes could be:
                    def is_greater_node(node1, node2):
                        return node1.val > node2.val
                        
        Credit: https://www.geeksforgeeks.org/priority-queue-in-python/
        """
        self.is_greater_func = is_greater_func if is_greater_func \
                                            else lambda x,y: x > y
        self.queue = []
    
    def __str__(self):
        """ Prints out the priority queue for debugging purposes. """
        return str(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def push(self, data):
        """ Inserts `data` of appropriate type (must be comparable  
            using `self.is_greater_func`)"""
        self.queue.append(data)
    
    def pop(self):
        """ Deletes a `data` instance and return it. """
        if self.isEmpty():
            return None
        max = 0
        for i in range(len(self.queue)):
            if self.is_greater_func(self.queue[i], self.queue[max]):
                max = i
        item = self.queue[max]
        del self.queue[max]
        return item
    
def is_greater_func(x, y):
    d = {x : p for x, p in zip(["i", "o", "u", "s", "r"], range(5))}
    return d[x] > d[y]

# Driver code for testing
if __name__ == "__main__":
    cases = [
        [1, 3, 5, 7, 9, 2, 4, 6, 8, 0],
        ["i", "o", "u", "s", "r"]
    ]

    for i, case in enumerate(cases):
        if i == 0:
            pq = PQDummy()
        else:
            pq = PQDummy(is_greater_func)
        for value in case:
            pq.push(value)
        result = [pq.pop() for i in range(len(case))]

        print("Correct output is:", result)
        