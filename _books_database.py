# 	Abby Gervase, Grace Milton, and Roann Yanes
# 	_books_database.py -- OO API
# 	November 29, 2017

import collections

class _books_database:

    def __init__(self):
        self.books = {}
        self.authors = collections.defaultdict(set)
        self.ratings = {}
        self.images = {}
        self.genres = collections.defaultdict(set)

    # load books from csv file into dictionaries
    def load_books(self, book_file):
        file_open = open(book_file, "r")
        for line in file_open:
            book_line = line.strip().split(",")
            # read in when multiple authors exist
            if book_line[7].startswith("\""):
                author_list = []
                # stores first author
                author_list.append(book_line[7][1:])
                self.authors[book_line[7][1:]].add(int(book_line[1]))
                i = 8
                # stores middle author
                while not book_line[i].endswith("\""):
                    author_list.append(book_line[i])
                    self.authors[book_line[i]].add(int(book_line[1]))
                    i += 1
                # stores last author
                author_list.append(book_line[i][:-1])
                self.authors[book_line[i][:-1]].add(int(book_line[1]))
                year = book_line[i + 1]
                if year:
                    year = int(float(year))
                self.books[int(book_line[1])] = [author_list, year, book_line[i + 2]]
                self.images[int(book_line[1])] = book_line[i + 15]
            # read in when single author
            else:
                year = book_line[8]
                if year:
                    year = int(float(year))
                self.books[int(book_line[1])] = [[book_line[7]], year, book_line[9]]
                self.images[int(book_line[1])] = book_line[22]
                self.authors[book_line[7]].add(int(book_line[1]))
        file_open.close()

    # get book by goodreads id
    def get_book(self, bid):
        if bid in self.books:
            return (self.books[bid])
        else:
            return None

    # get list of all book ids
    def get_books(self):
        return [int(x) for x in list(self.books)]

    # sets book
    def set_book(self, bid, books):
        self.books[bid] = books

    # deletes book
    def delete_book(self, bid):
        del self.books[bid]
    
    # returns list of books published in given year
    def get_books_by_year(self, year):
        year_list = []
        for bid in self.books:
            if self.books[bid][1] == year:
                year_list.append(bid)
        return year_list

    # loads different genres with a list of books in each genre
    def load_genres(self, genres_file):
        file_open = open(genres_file, "r")
        for line in file_open:
            info = line.strip().split(",")
            self.genres[int(info[1])].add(int(info[0]))
        file_open.close()
    
    # returns set of books classified under a given genre
    def get_books_by_genre(self, genre):
        if genre in self.genres:
            return self.genres[genre]
        else:
            return None
    
    def load_ratings(self, ratings_file):
        file_open = open(ratings_file, "r")
        for line in file_open:
            info = line.strip().split(",")
            if int(info[0]) not in self.ratings:
                self.ratings[int(info[0])] = {}
            self.ratings[int(info[0])].update({int(info[1]): float(info[2])})
        file_open.close()

    def get_rating(self, bid):
        if bid in self.ratings:
            return sum(self.ratings[bid].values())/len(self.ratings[bid])
        else:
            return 0

    def get_highest_rated_book(self):
        highest = 0
        top = 0
        for bid in self.ratings:
            if self.get_rating(int(bid)) > highest:
                highest = self.get_rating(int(bid))
                top = bid
            elif self.get_rating(int(bid)) == highest and bid < top:
                highest = self.get_rating(int(bid))
                top = bid
        if highest > 0:
            return top
        else:
            return None
   
    def set_user_book_rating(self, uid, bid, rating):
        self.ratings[bid].update({uid: rating})
 
    def get_user_book_rating(self, uid, bid):
        return self.ratings[bid][uid]

    def delete_all_ratings(self):
        self.ratings = {}

    def load_images(self, image_file):
        for line in open(image_file, "r"):
            self.images[int(line.split("::")[0])] = line.strip().split("::")[2]

    def get_image(self, bid):
        if bid in self.images:
            return (self.images[bid])
        else:
            return None

    def set_image(self, mid, image):
        self.images[mid] = image
	
    def get_highest_rated_unvoted_movie(self, uid):
        for mid in self.movies:
            self.recommendations[mid] = self.get_rating(mid)
        temp = sorted(self.recommendations, key=self.recommendations.get, reverse=True)
        i = 0
        while i < len(temp):
            max_mid = temp[i]
            if uid not in self.ratings[max_mid]:
                return max_mid
            else:
                i += 1

if __name__ == "__main__":
    bdb = _book_database()
    bdb.load_books('book_files/books.csv')
    print(bdb.get_books())
