import unittest
import bst

class TestBSTAppendMethod(unittest.TestCase):

    def setUp(self):
        self.bt = bst.BinaryTree(5)

    def test_append_one_node(self):
        self.bt.append(10)
        self.assertEqual(self.bt.root.right.data, 10)

    def test_append_two_node(self):
        self.bt.append(2)
        self.assertEqual(self.bt.root.left.data, 2)

if __name__ == '__main__':
    unittest.main()