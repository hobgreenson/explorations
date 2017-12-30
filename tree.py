import time

class Heap:
    def __init__(self, data, minheap=True):
        self.data = data
        self.minheap = minheap 


class Node:
    """ Tree node.
    """
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.key)


class BinarySearchTree:
    """ This is a basic binary search tree (NOT self-balancing).
    More advanced trees might use this as a base class.
    """
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __contains__(self, key):
        node = self.root
        while node is not None:
            if key == node.key:
                return True
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return False

    def __getitem__(self, key):
        """ Retrieve the data contained in the node
        with matching key, otherwise raise KeyError if
        no key matches.
        """
        node = self.root
        while node is not None:
            if key == node.key:
                return node.data
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        raise KeyError

    def __setitem__(self, key, value):
        """ Insert a new node into the tree. If there is an
        existing node with a matching key, then the data in that
        node is replaced.
        """
        if self.root is None:
            self.root = Node(key, value)
        else:
            node = self.root
            while True:
                if key == node.key:
                    node.data = value
                    break
                elif key < node.key:
                    if node.left is None:
                        node.left = Node(key, value)
                        break
                    else:
                        node = node.left
                else:
                    if node.right is None:
                        node.right = Node(key, value)
                        break
                    else:
                        node = node.right
        self.size += 1

    def __delitem__(self, key):
        """ Deletes a node from the tree. If the left
        subtree is not empty, then the node is replaced
        with the node with the largest key in the left
        subtree. If the left subtree is empty, and the right
        subtree is not empty, then the node is replaced with
        the smallest node in the right subtree. If both left
        and right subtrees are empty, then the node is not
        replaced with anything.
        """
        prev = None
        curr = self.root
        while curr is not None:
            if key == curr.key:
                break     
            elif key < curr.key:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        
        raise KeyError

    def keys(self):
        """ Returns a list of node keys in ascending 
        sorted order. A stack called 'visited' is maintained,
        which keeps track of the history of visted nodes. A
        pointer to a node is advanced left, and visted nodes
        are pushed onto the stack, until the node points to None,
        indicating that the last-visted 
        """
        keys = []
        if self.root is None: return keys
        visited = [self.root]
        node = self.root.left
        while len(visited) > 0:
            if node is not None:
                visited.append(node)
                node = node.left
            else:
                parent = visited.pop()
                keys.append(parent.key)
                if parent.right is not None:
                    visited.append(parent.right)
                    node = parent.right.left
        return keys 

def test_binary_search_tree():
    tree = BinarySearchTree()
    assert len(tree) == 0
    tree['g'] = 1
    assert len(tree) == 1
    assert 'g' in tree
    assert tree['g'] == 1
    tree['c'] = 2
    assert len(tree) == 2
    assert 'c' in tree
    assert tree['c'] == 2
    tree['j'] = 3
    assert len(tree) == 3
    assert 'j' in tree
    assert tree['j'] == 3
    assert tree.root.key == 'g'
    assert tree.root.left.key == 'c'
    assert tree.root.right.key == 'j'
    assert tree.keys() == ['c', 'g', 'j']


if __name__ == '__main__':
    test_binary_search_tree()

