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
        self.voted_books = {}
        self.recommendations = {}
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
                self.ratings[int(book_line[1])] = list(map(int, book_line[-7:-2]))
                self.images[int(book_line[1])] = book_line[-2]
            # read in when single author
            else:
                year = book_line[8]
                if year:
                    year = int(float(year))
                self.books[int(book_line[1])] = [[book_line[7]], year, book_line[9]]
                self.ratings[int(book_line[1])] = list(map(int, book_line[-7:-2]))
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

    # gets the average rating of the book
    def get_rating(self, bid):
        if bid in self.ratings:
total = 0
            total += self.ratings[bid][0]
            total += 2*self.ratings[bid][1]
            total += 3*self.ratings[bid][2]
            total += 4*self.ratings[bid][3]
            total += 5*self.ratings[bid][4]
            return total/sum(self.ratings[bid])
        else:
            return 0

    # retrieves the highest rated book
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

    # updates the user's book rating
    def set_book_rating(self, bid, rating):
        if rating != 0:
            if bid in self.voted_books:
                self.ratings[bid][self.voted_books[bid] - 1] -= 1
            self.ratings[bid][rating - 1] += 1
            self.voted_books.update({bid: rating})
 
    # gets the user's rating for a particular book 
    def get_user_book_rating(self, bid):
        if bid in self.voted_books:
            return self.voted_books[bid]
        else:
            return None
    
    # deletes all the ratings
    def delete_all_ratings(self):
        self.ratings = {}
        self.voted_books = {}

    # retrieves the image url of the book cover
    def get_image(self, bid):
        if bid in self.images:
            return (self.images[bid])
        else:
            return None

    # sets the image url of the book cover
    def set_image(self, bid, image):
        self.images[bid] = image
	
    # returns the highest rated unvoted book that the user has not voted on yet
    def get_highest_rated_unvoted_book(self, num_books):
        for bid in self.books:
            self.recommendations[bid] = self.get_rating(bid)
        temp = sorted(self.recommendations, key=self.recommendations.get, reverse=True)
        i = 0
        max_bid = []
        while i < len(temp) and len(max_bid) < num_books:
            if temp[i] not in self.voted_books:
                max_bid.append(temp[i])
            i += 1
        return max_bid
