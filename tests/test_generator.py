import itertools
import unittest
import warnings

from halfrand import HalfRandom, generate, randomNum


class GenerateTests(unittest.TestCase):
    def test_seed_makes_results_reproducible(self):
        self.assertEqual(generate(10, seed=42), generate(10, seed=42))

    def test_adjacent_values_respect_step(self):
        values = generate(100, step=0.025, seed=4)
        self.assertTrue(all(abs(a - b) <= 0.025 for a, b in itertools.pairwise(values)))

    def test_bounds_are_respected(self):
        values = generate(1_000, step=0.5, seed=2, start=0.5, lower=0.25, upper=0.75)
        self.assertTrue(all(0.25 <= value <= 0.75 for value in values))

    def test_empty_sequence(self):
        self.assertEqual(generate(0), [])

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            generate(-1)
        with self.assertRaises(TypeError):
            generate(1.5)  # type: ignore[arg-type]
        with self.assertRaises(ValueError):
            HalfRandom(step=-1)
        with self.assertRaises(ValueError):
            HalfRandom(lower=2, upper=1)

    def test_iterator(self):
        values = list(itertools.islice(HalfRandom(seed=3).iter(start=0.5), 4))
        self.assertEqual(values[0], 0.5)
        self.assertEqual(len(values), 4)

    def test_legacy_api_warns(self):
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            self.assertEqual(len(randomNum(3)), 3)
        self.assertEqual(caught[0].category, DeprecationWarning)


if __name__ == "__main__":
    unittest.main()
