from django.test import TestCase

from weighted_sort.sort import sort, get_normalize_function


class TestWeightedSorting(TestCase):
    def test_sort_empty_sequence_returns_empty_sequence(self):
        self.assertEqual(sort([]), [])

    def test_sort_return_one_element_array(self):
        e = {"id": 1, "foo": "something", "bar": "something else"}
        self.assertEqual(sort([e]), [e])

    def test_sort_return_sorted_sequence(self):
        sequence = [5, 3, 1, 4, -3]
        expected = [-3, 1, 3, 4, 5]
        self.assertEqual(sort(sequence), expected)

    def test_sort_sorts_by_key(self):
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

    def test_sort_does_normalized_weighted_sort(self):
        sequence = [
            {"foo": 0, "bar": 2, "baz": 1},
            {"foo": 10, "bar": 0, "baz": 1},
            {"foo": 20, "bar": 1, "baz": 1},
        ]
        expected = sorted(sequence, key=lambda e: e["foo"]/10 + e["bar"]*2)
        self.assertEqual(sort(sequence, {"foo": 1, "bar": 2}), expected)

    def test_normalizer_function(self):
        seq = [1, 5, 25]
        normalize = get_normalize_function(seq)
        self.assertEqual(normalize(seq[0]), 0)
        self.assertEqual(normalize(5),  1 / 6)
        self.assertEqual(normalize(seq[-1]), 1)

    def test_normalizer_function_for_negative_values(self):
        seq = [-10, 5, 10]
        normalize = get_normalize_function(seq)
        self.assertEqual(normalize(seq[0]), 0)
        self.assertEqual(normalize(5),  15 / 20)
        self.assertEqual(normalize(seq[-1]), 1)

