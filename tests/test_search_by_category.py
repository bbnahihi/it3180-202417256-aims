import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category_ignores_case(self):
        items = [DigitalVideoDisc("The Lion King", "Animation"),
                 DigitalVideoDisc("Star Wars", "Science Fiction")]
        found = search_by_category(items, "animation")
        self.assertEqual([dvd.title for dvd in found], ["The Lion King"])


if __name__ == "__main__":
    unittest.main()
