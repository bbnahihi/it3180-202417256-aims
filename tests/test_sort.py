import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        for title, cost in [("Star Wars", 24.95), ("Aladdin", 18.99), ("The Lion King", 19.95)]:
            self.cart.add_dvd(DigitalVideoDisc(title, cost=cost))

    def test_sort_by_title(self):
        titles = [dvd.title for dvd in self.cart.sort_by_title()]
        self.assertEqual(titles, ["Aladdin", "Star Wars", "The Lion King"])

    def test_sort_by_cost(self):
        costs = [dvd.cost for dvd in self.cart.sort_by_cost()]
        self.assertEqual(costs, [24.95, 19.95, 18.99])


if __name__ == "__main__":
    unittest.main()
