import unittest
import merge_sort_1

class TestMergeSortStorageIssue(unittest.TestCase):

    def test_sort_reverse_sorted_list(self):
        reverse_sorted = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        sorted_list = merge_sort_1.CopyMergeSort(reverse_sorted)

        self.assertEqual(expected, sorted_list)


    def test_sort_sorted_list(self):
        sorted_list = [1, 2, 3, 3, 5, 6, 6, 8, 23, 34, 90]
        expected = [1, 2, 3, 3, 5, 6, 6, 8, 23, 34, 90]

        sorted_list = merge_sort_1.CopyMergeSort(sorted_list)

        self.assertEqual(expected, sorted_list)

    def test_sort_empty_list(self):
        empty = []
        expected = []

        sorted_list = merge_sort_1.CopyMergeSort(empty)

        self.assertEqual(expected, sorted_list)


    def test_sort_unsorted_list(self):
        unsorted = [6, 23, 8, 34, 90, 1, 3, 5, 3, 2, 6]
        expected = [1, 2, 3, 3, 5, 6, 6, 8, 23, 34, 90]

        sorted_list = merge_sort_1.CopyMergeSort(unsorted)

        self.assertEqual(expected, sorted_list)

    def test_sort_list_has_duplicates(self):
        unsorted = [6, 23, 8, 34, 90, 1, 3, 23, 5, 3, 2, 6, 90]
        expected = [1, 2, 3, 3, 5, 6, 6, 8, 23, 23, 34, 90, 90]

        sorted_list = merge_sort_1.CopyMergeSort(unsorted)

        self.assertEqual(expected, sorted_list)


if __name__ == '__main__':
    unittest.main()