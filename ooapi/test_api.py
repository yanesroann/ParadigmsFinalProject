from _books_database import _books_database
import unittest

class TestBookDatabase(unittest.TestCase):
        """unit tests for python primer homework"""

        #@classmethod
        #def setUpClass(self):
        bdb = _books_database()

        def reset_data(self):
                "reset data is required because we cannot promise an order of test case execution"
                self.bdb.delete_all_ratings()
                self.bdb.load_books('book_files/books.csv')
                self.bdb.load_genres('book_files/book_tags.csv')

        def test_get_book(self):
                self.reset_data()
                book = self.bdb.get_book(2767052)
                self.assertEqual(book[0][0], 'Suzanne Collins')
                self.assertEqual(book[1], 2008)
                self.assertEqual(book[2], 'The Hunger Games')

        def test_get_book_null(self):
                self.reset_data()
                book = self.bdb.get_book(200000000)
                self.assertEqual(book, None)
        
        def test_get_books_by_year(self):
                self.reset_data()
                year_list = self.bdb.get_books_by_year(1897)
                self.assertEqual(year_list[0], 17245)
                self.assertEqual(year_list[1], 17184)
                self.assertEqual(year_list[2], 15638)
                self.assertEqual(year_list[3], 34057)
                self.assertEqual(year_list[4], 231560)
                self.assertEqual(year_list[5], 8909)
        
        def test_get_books_by_genre(self):
                self.reset_data()
                genre_list = list(self.bdb.get_books_by_genre(15306))
                self.assertEqual(genre_list[0], 8)
        
        def test_get_image(self):
                self.reset_data()
                image = self.bdb.get_image(41865)
                self.assertEqual(image, "https://images.gr-assets.com/books/1361039443m/41865.jpg")

        def test_set_image(self):
                self.reset_data()
                self.bdb.set_image(41865, 'Grace')
                image = self.bdb.get_image(41865)
                self.assertEqual(image, 'Grace')
        
        def test_set_book(self):
                self.reset_data()
                book = self.bdb.get_book(84847)
                book[2] = 'Abby'
                self.bdb.set_book(84847, book)
                book = self.bdb.get_book(84847)
                self.assertEqual(book[2], 'Abby')

        def test_delete_book(self):
                self.reset_data()
                self.bdb.delete_book(8909)
                book = self.bdb.get_book(8909)
                self.assertEqual(book, None)

        def test_get_rating(self):
                self.reset_data()
                rating = self.bdb.get_rating(13152)
                self.assertEqual(round(rating, 2), 4.08)
                rating = self.bdb.get_rating(33313)
                self.assertEqual(round(rating, 2), 4.0)

        def test_get_highest_rated_book(self):
                self.reset_data()
                hrb_bid = self.bdb.get_highest_rated_book()
                hrb_rating = self.bdb.get_rating(hrb_bid)
                hrb = self.bdb.get_book(hrb_bid)
                hrb_name = hrb[2]
                self.assertEqual(hrb_bid, 24812)
                self.assertEqual(hrb_name, 'The Complete Calvin and Hobbes')
                self.assertEqual(round(hrb_rating, 2), 4.82)

        def test_get_user_book_rating(self):
                self.reset_data()
                rating = self.bdb.get_rating(209194)
                self.assertEqual(rating, 4.25)

        def test_set_and_get_book_ratings(self):
                self.reset_data()
                self.bdb.set_book_rating(5352, 5)
                hrb_bid = self.bdb.get_highest_rated_book()
                hrb_rating = self.bdb.get_rating(hrb_bid)
                hrb = self.bdb.get_book(hrb_bid)
                hrb_name = hrb[2]
                self.assertEqual(hrb_bid, 24812)
                self.assertEqual(hrb_name, 'The Complete Calvin and Hobbes')
                self.assertEqual(round(hrb_rating, 2), 4.82)

        def test_get_user_book_rating(self):
                self.reset_data()
                rating = self.bdb.get_user_book_rating(6030)
                self.assertEqual(rating, None)

if __name__ == "__main__":
    unittest.main()

