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
        self.is_greater_func = is_greater_func if not is_greater_func \
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
    
    
class PQAdjaciencyMatrix(PriorityQueue):
    def __init__(self, is_greater_func=None):
        """
        Priority Queue implemented with Adjaciency Matrix. 
        
        Arguments:
        is_greater_func: (Optional) Function to compare datatypes 
                    used in algorithm. E.g: A function to compare 
                    nodes could be:
                    def is_greater_node(node1, node2):
                        return node1.val > node2.val
        """
        super(PQAdjaciencyMatrix).__init__(is_greater_function=is_greater_function)
        self.matrix = [[]]
    
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
        super(PQBinaryHeap).__init__(is_greater_function=is_greater_function)
        self.matrix = [[]]
    
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
    
    
class PQFibonacciHeap(PriorityQueue):
    def __init__(self, is_greater_func=None):
        """
        Priority Queue implemented with Fibonacci Heap. 
        
        Arguments:
        is_greater_func: (Optional) Function to compare datatypes 
                    used in algorithm. E.g: A function to compare 
                    nodes could be:
                    def is_greater_node(node1, node2):
                        return node1.val > node2.val
        """
        super(PQFibonacciHeap).__init__(is_greater_function=is_greater_function)
        self.matrix = [[]]
    
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
    

# Driver code for testing
if __name__ == "__main__":
    cases = [
        [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    ]

    for case in cases:
        h = []
        for value in case:
            heappush(h, value)
        correct_result = [heappop(h) for i in range(len(h))]

    #     pq = PQAdjaciencyMatrix()
    #     for value in case:
    #         pq.push(value)
    #     result = [pq.pop() for i in range(len(h))]