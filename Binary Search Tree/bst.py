class TreeNode():
    """
    Binary Tree Node
    """
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def append(self, data):
        """
        Add new node to the node
        """
        if data <= self.data:
            if self.left is None:
                self.left = TreeNode(data)
            else:
                self.left.append(data)
        else:
            if self.right is None:
                self.right = TreeNode(data)
            else:
                self.right.append(data)

    def delete(self, data):
        """
        Delete node with data and return the node will subtitue it
        """
        if self.right == self.left == None:
            return None
        elif self.right is None:
            return self.left
        elif self.left is None:
            return self.right

        child = self.left
        grandchild = child.right
        if grandchild:
            while grandchild.right:
                child = grandchild
                grandchild = grandchild.right
            self.data = grandchild.data
            child.right = grandchild.left
        else:
            self.left = child.left
            self.data = child.data

        return self



class BinaryTree():
    """
    Binary Tree
    """
    def __init__(self, root):
        self.root = TreeNode(root)

    def append(self, data):
        """
        Add node to binary tree
        """
        self.root.append(data)

    def find(self, data):
        """
        Search for node in the tree by its value
        """
        node = self.root
        while node:
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        else:
            raise IndexError("Node is not exists")

    def delete(self, data):
        """
        Delete node from the tree
        """
        if self.root:
            self.root = self.deleteFromParent(self.root, data)

    def deleteFromParent(self, parent, data):
        """
        Remove node from tree rooted at parent
        """
        if parent is None:
            return None

        if data == parent.data:
            return parent.delete(data)
        elif data < parent.data:
            parent.left = self.deleteFromParent(parent.left, data)
        else:
            parent.right = self.deleteFromParent(parent.right, data)

        return parent
