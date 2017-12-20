
class Node:
    """ Tree node.
    """
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None


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
        prev = None
        curr = self.root
        while curr is not None:
            if key == curr.key:
                if curr.left is None and curr.right is None:
                   pass 
            elif key < curr.key:
                prev = curr
                curr = curr.left
            else:
                prev = curr
                curr = curr.right
        raise KeyError


def test_trees():
    tree = BinarySearchTree()
    assert len(tree) == 0
    tree['a'] = 1
    assert len(tree) == 1
    assert 'a' in tree
    assert tree['a'] == 1
    tree['b'] = 2
    assert len(tree) == 2
    assert 'b' in tree
    assert tree['b'] == 2
    assert tree.root.right.key == 'b'
    assert tree.root.right.data == 2


if __name__ == '__main__':
    test_trees()

