# Modified HashSet class to fit Prim's algorithm requirements.
# Removing an item from this set is impossible. This minimizes space of algorithm, as remove is not needed during prim's runtime

# Checker for handling items in set
class Checker:
    # Basic __init__ function to start array
    def __init__(self):
        self.list = []

    # Function to update array
    def update(self, key):
        contained = False
        i = 0

        for k in self.list:
            if key == k:
                self.list[i] = key
                contained = True
                break
        if contained == False:
            self.list.append(key)

    # Function to check key inclusion
    def get(self, key):
        for k in self.list:
            if k == key:
                return True
            return False

# HashSet class for hasifying set
class HashSet:
    def __init__(self):
        # Number needed for Keyspace found online
        self.key_space = 2096
        self.set = [Checker() for i in range(self.key_space)]

    # Method for adding element to set
    def add(self, key):
        hash_key = key % self.key_space
        self.set[hash_key].update(key)

    # Method for checking if key contained in set
    def contains(self, key):
        hash_key = key % self.key_space
        return self.set[hash_key].get(key)




