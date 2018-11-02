import unittest
import deck_oop


class CardTest(unittest.TestCase):
    def setUp(self):
        self.suit = 'T'
        self.rank = 2
        self.weight = 5
        self.card = deck_oop.Card(self.suit, self.rank)

    def test_check_init(self):
        self.assertEqual(self.card.suit, self.suit)
        self.assertEqual(self.card.rank, self.rank)
        self.assertIsNone(self.card.weight)

    def test_check_init2(self):
        self.assertEqual(self.card.suit, self.suit)
        self.assertEqual(self.card.rank, self.rank)
        self.assertIsNone(self.card.weight)

    def test_check_init3(self):
        self.assertEqual(self.card.suit, self.suit)
        self.assertNotEqual(self.card.rank, str(self.rank))
        self.assertIsNone(self.card.weight)

    def test_check_weight(self):
        self.card.weight = self.weight
        self.assertEqual(self.card.weight, self.weight)

    def test_check_repr(self):
        temp = '{}{}'.format(self.rank, self.suit)
        self.assertEqual(self.card.__repr__(), temp)


if __name__ == "__name__":
    unittest.main()
