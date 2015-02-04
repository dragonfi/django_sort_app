from django.test import TestCase

from weighted_sort.sort import sort


class TestWeightedSorting(TestCase):
    def test_sort_return_one_element_array(self):
        e = {"id": 1, "foo": "something", "bar": "something else"}
        self.assertEqual(sort([e]), [e])

    def test_sort_return_sorted_sequence(self):
        sequence = [5, 3, 1, 4, -3]
        expected = [-3, 1, 3, 4, 5]
        self.assertEqual(sort(sequence), expected)

    def test_sort_sorts__by_key(self):
        sequence = [
            {"foo": 3, "bar": 2, "baz": 1},
            {"foo": 10, "bar": 0, "baz": 1},
            {"foo": 5, "bar": 1, "baz": 1},
        ]
        expected = sorted(sequence, key=lambda e: e["foo"])
        self.assertEqual(sort(sequence, {"foo": 1}), expected)

    def test_sort_does_weighted_sort_for_multiple_keys(self):
        sequence = [
            {"foo": 0, "bar": 2, "baz": 1},
            {"foo": 1, "bar": 0, "baz": 1},
            {"foo": 2, "bar": 1, "baz": 1},
        ]
        expected = sorted(sequence, key=lambda e: e["foo"] + e["bar"]*2)
        self.assertEqual(sort(sequence, {"foo": 1, "bar": 2}), expected)

