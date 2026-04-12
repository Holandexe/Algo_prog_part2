import unittest

def find_kth_largest(arr, k):
    if len(arr) == 0:
        raise ValueError("array is empty")
    if k > len(arr) or k < 1:
        raise ValueError("k is out of range")

    temp = []
    for i in range(len(arr)):
        temp.append((arr[i], i))

    def merge(lst, left, mid, right):
        left_part = []
        for i in range(left, mid + 1):
            left_part.append(lst[i])

        right_part = []
        for i in range(mid + 1, right + 1):
            right_part.append(lst[i])

        li = 0
        ri = 0
        idx = left
        while li < len(left_part) and ri < len(right_part):
            if left_part[li][0] >= right_part[ri][0]:
                lst[idx] = left_part[li]
                li += 1
            else:
                lst[idx] = right_part[ri]
                ri += 1
            idx += 1

        while li < len(left_part):
            lst[idx] = left_part[li]
            li += 1
            idx += 1

        while ri < len(right_part):
            lst[idx] = right_part[ri]
            ri += 1
            idx += 1

    def merge_sort(lst, left, right):
        if left >= right:
            return

        mid = (left + right) // 2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
        merge(lst, left, mid, right)

    merge_sort(temp, 0, len(temp) - 1)

    value = temp[k - 1][0]
    index = temp[k - 1][1]

    return value, index


def print_result(arr, k):
    value, index = find_kth_largest(arr, k)
    print(f"Array: {arr}")
    print(f"k: {k}")
    print(f"The {k}-th largest element: {value}")
    print(f"Index of the {k}-th largest element: {index}")


class TestFindKthLargest(unittest.TestCase):

    def test_example(self):
        arr = [15, 7, 22, 9, 36, 2, 42, 18]
        value, index = find_kth_largest(arr, 3)
        self.assertEqual(value, 22)
        self.assertEqual(index, 2)

    def test_k1_is_max(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        value, index = find_kth_largest(arr, 1)
        self.assertEqual(value, 9)
        self.assertEqual(index, 5)

    def test_k_last_is_min(self):
        arr = [10, 20, 30]
        value, index = find_kth_largest(arr, 3)
        self.assertEqual(value, 10)
        self.assertEqual(index, 0)

    def test_one_element(self):
        arr = [42]
        value, index = find_kth_largest(arr, 1)
        self.assertEqual(value, 42)
        self.assertEqual(index, 0)

    def test_negative(self):
        arr = [-5, -1, -3, -2, -4]
        value, index = find_kth_largest(arr, 2)
        self.assertEqual(value, -2)
        self.assertEqual(index, 3)

    def test_k_too_big(self):
        with self.assertRaises(ValueError):
            find_kth_largest([1, 2, 3], 5)

    def test_empty(self):
        with self.assertRaises(ValueError):
            find_kth_largest([], 1)


if __name__ == "__main__":
    print_result([15, 7, 22, 9, 36, 2, 42, 18], 3)
    print()
    unittest.main(verbosity=2) 