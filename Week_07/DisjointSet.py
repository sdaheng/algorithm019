import unittest

class DisjointSet:
    """
    
    """
    def __init__(self, capacity) -> None:
        self.array = [ i for i in range(capacity) ]

    def union(self, i, j):
        """
        docstring
        """
        
        p1 = self.parent(i)
        p2 = self.parent(j)

        self.array[p1] = p2

    def parent(self, i):
        """
        docstring
        """
        root = i
        while self.array[root] != root:
            root = self.array[root]

        while self.array[i] != i:
            x = i
            i = self.array[i]
            self.array[x] = root

        return root
    
    def connected(self, i, j):
        """
        docstring
        """
        p1 = self.parent(i)
        p2 = self.parent(j)
        return p1 == p2

class Test(unittest.TestCase):
    def testUnion(self):
        """
        
        """
        disjointSet = DisjointSet(5)

        disjointSet.union(2, 3)

        self.assertTrue(disjointSet.connected(2, 3))
        
if __name__ == "__main__":
    unittest.main()
