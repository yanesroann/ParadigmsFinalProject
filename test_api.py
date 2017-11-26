from _books_database import _books_database
import unittest

class TestBookDatabase(unittest.TestCase):
        """unit tests for python primer homework"""

        #@classmethod
        #def setUpClass(self):
        bdb = _books_database()

        def reset_data(self):
                "reset data is required because we cannot promise an order of test case execution"
                #self.mdb.delete_all_ratings()
                self.bdb.load_books('book_files/books.csv')
                self.bdb.load_genres('book_files/book_tags.csv')
                #self.mdb.load_ratings('ml-1m/ratings.dat')

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
        
"""        def test_set_user(self):
                self.reset_data()
                user = self.mdb.get_user(3)
                user[2] = 6
                self.mdb.set_user(3, user)
                user = self.mdb.get_user(3)
                self.assertEquals(user[1], 25)
                self.assertEquals(user[2], 6)
                self.assertEquals(user[3], '55117')

        def test_delete_user(self):
                self.reset_data()
                self.mdb.delete_user(3)
                user = self.mdb.get_user(3)
                self.assertEquals(user, None)

        def test_get_rating(self):
                self.reset_data()
                rating = self.mdb.get_rating(32)
                self.assertEquals(rating, 3.945731303772336)
                rating = self.mdb.get_rating(110)
                self.assertEquals(rating, 4.234957020057307)
                rating = self.mdb.get_rating(1)
                self.assertEquals(rating, 4.146846413095811)

        def test_get_highest_rated_movie_1(self):
                self.reset_data()
                hrm_mid = self.mdb.get_highest_rated_movie()
                hrm_rating = self.mdb.get_rating(hrm_mid)
                hrm = self.mdb.get_movie(hrm_mid)
                hrm_name = hrm[0]
                self.assertEquals(hrm_mid, 787)
                self.assertEquals(hrm_name, 'Gate of Heavenly Peace, The (1995)')
                self.assertEquals(hrm_rating, 5.0)

        def test_set_user_movie_rating_1(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                rating = self.mdb.get_rating(787)
                self.assertEquals(rating, 4.25)

        def test_set_user_movie_rating_2(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                self.mdb.set_user_movie_rating(101, 787, 4)
                rating = self.mdb.get_rating(787)
                self.assertEquals(rating, 4.2)

        def test_set_and_get_movie_ratings(self):
                self.reset_data()
                self.mdb.set_user_movie_rating(41, 787, 2)
                self.mdb.set_user_movie_rating(101, 787, 4)
                hrm_mid = self.mdb.get_highest_rated_movie()
                hrm_rating = self.mdb.get_rating(hrm_mid)
                hrm = self.mdb.get_movie(hrm_mid)
                hrm_name = hrm[0]
                self.assertEquals(hrm_mid, 989)
                self.assertEquals(hrm_name, 'Schlafes Bruder (Brother of Sleep) (1995)')
                self.assertEquals(hrm_rating, 5.0)

        def test_get_user_movie_rating(self):
                self.reset_data()
                rating = self.mdb.get_user_movie_rating(6030, 32)
                self.assertEquals(rating, 5)
"""
if __name__ == "__main__":
    unittest.main()

