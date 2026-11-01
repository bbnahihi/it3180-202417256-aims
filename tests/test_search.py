import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):
    def test_search_by_title_ignores_case(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Star Wars")]
        found = search_by_title(items, "lion")
        self.assertEqual([dvd.title for dvd in found], ["The Lion King"])


if __name__ == "__main__":
    unittest.main()
