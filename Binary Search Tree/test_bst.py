import unittest
import bst

class TestBSTAppendMethod(unittest.TestCase):

    def setUp(self):
        self.bt = bst.BinaryTree(5)

    def test_append_one_node(self):
        self.bt.append(10)
        node1 = self.bt.find(10)
        self.assertEqual(node1.data, 10)

    def test_append_two_nodes(self):
        self.bt.append(10)
        self.bt.append(2)

        node1 = self.bt.find(10)
        node2 = self.bt.find(2)

        self.assertEqual(node1.data, 10)
        self.assertEqual(node2.data, 2)

    def test_append_three_nodes(self):
        self.bt.append(10)
        self.bt.append(2)
        self.bt.append(3)

        node1 = self.bt.find(10)
        node2 = self.bt.find(2)
        node3 = self.bt.find(3)

        self.assertEqual(node1.data, 10)
        self.assertEqual(node2.data, 2)
        self.assertEqual(node3.data, 3)

    def test_append_four_nodes(self):
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


class TestBSTFindMethod(unittest.TestCase):

    def setUp(self):
        self.bt = bst.BinaryTree(5)

    def test_find_one_node(self):
        self.bt.append(10)

        node1 = self.bt.find(10)

        self.assertEqual(node1.data, 10)

    def test_find_two_nodes(self):
        self.bt.append(10)
        self.bt.append(2)


        node1 = self.bt.find(10)
        node2 = self.bt.find(2)


        self.assertEqual(node1.data, 10)
        self.assertEqual(node2.data, 2)

    def test_find_four_nodes(self):
        self.bt.append(10)
        self.bt.append(2)
        self.bt.append(3)

        node1 = self.bt.find(10)
        node2 = self.bt.find(2)
        node3 = self.bt.find(3)

        self.assertEqual(node1.data, 10)
        self.assertEqual(node2.data, 2)
        self.assertEqual(node3.data, 3)

    def test_find_four_nodes(self):
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


class TestBSTDeleteMethod(unittest.TestCase):

    def setUp(self):
        self.bt = bst.BinaryTree(5)

    def test_delete_root_node(self):
        self.bt.delete(5)

        self.assertIsNone(self.bt.root)

    def test_delete_node_with_no_child(self):
        self.bt.append(10)
        self.bt.delete(10)

        self.assertRaises(IndexError, lambda: self.bt.find(10))

    def test_delete_node_with_right_child(self):
        self.bt.append(10)
        self.bt.append(12)
        self.bt.delete(12)

        self.assertRaises(IndexError, lambda: self.bt.find(12))

    def test_delete_node_with_left_child(self):
        self.bt.append(10)
        self.bt.append(12)
        self.bt.append(11)
        self.bt.delete(11)

        self.assertRaises(IndexError, lambda: self.bt.find(11))

    def test_delete_node_with_left_and_right_child(self):
        self.bt.append(10)
        self.bt.append(12)
        self.bt.append(11)
        self.bt.delete(10)

        self.assertRaises(IndexError, lambda: self.bt.find(10))

if __name__ == '__main__':
    unittest.main()