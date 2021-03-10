import unittest
from Query import librarian, book, issue


class unitTesting(unittest.TestCase):
    obj = librarian()
    obj1 = book()
    obj2 = issue()

    def test_librarian_add(self):
        result = self.obj.addlibrarian(
            'Anu', 'Shivakoti', 'a@gmail.com', 'a', 'a', '9860')
        self.assertTrue(result)

    def test_book_add(self):
        result = self.obj2.add_book('Treasure Island', 'Adventure', 'Charles')
        self.assertTrue(result)

    def test_book_delete(self):
        result = self.obj2.delete_book('1')
        self.assertNotEqual(result, False)

    def test_issue_fetch(self):
        result = self.obj3.fetch_issue()
        self.assertNotEqual(result, False)
