import unittest
import bst

class TestBSTAppendMethod(unittest.TestCase):

    def setUp(self):
        self.bt = bst.BinaryTree(5)

    def test_append_one_node(self):
        self.bt.append(10)
        node1 = self.bt.find(10)
        self.assertEqual(node1.data, 10)

    def test_append_two_node(self):
        self.bt.append(10)
        self.bt.append(2)

        node1 = self.bt.find(10)
        node2 = self.bt.find(2)

        self.assertEqual(node1.data, 10)
        self.assertEqual(node2.data, 2)

    def test_append_three_node(self):
        self.bt.append(10)
        self.bt.append(2)
        self.bt.append(3)

        node1 = self.bt.find(10)
        node2 = self.bt.find(2)
        node3 = self.bt.find(3)

        self.assertEqual(node1.data, 10)
        self.assertEqual(node2.data, 2)
        self.assertEqual(node3.data, 3)

    def test_append_four_node(self):
        self.bt.append(10)
        self.bt.append(2)
        self.bt.append(3)
        self.bt.append(6)

        node1 = self.bt.find(10)
        node2 = self.bt.find(2)
        node3 = self.bt.find(3)
        node4 = self.bt.find(6)

        self.assertEqual(node1.data, 10)
        self.assertEqual(node2.data, 2)
        self.assertEqual(node3.data, 3)
        self.assertEqual(node4.data, 6)


if __name__ == '__main__':
    unittest.main()