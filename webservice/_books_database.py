# 	Abby Gervase, Grace Milton, and Roann Yanes
# 	_books_database.py -- Webservice
# 	November 30, 2017

import collections
import csv

class _books_database:

    def __init__(self):
        self.books = {}
        self.authors = collections.defaultdict(set)
        self.author_ids = {}
        self.ratings = {}
        self.images = {}
        self.voted_books = {}
        self.recommendations = {}
        self.genres = collections.defaultdict(set)

    # load books from csv file into dictionaries
    def load_books(self, book_file):
        file_open = open(book_file, "r")

        with file_open as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='\"')
            for line in spamreader:
                authors = line[7].split(",")
                bid = int(line[1])
                for a in authors:
                    if a not in self.author_ids:
                        self.author_ids[a] = len(self.author_ids)
                    author_id = self.author_ids[a]
                    self.authors[author_id].add(int(bid))
                if line[8]:
                    year = int(float(line[8]))
                else:
                    year = None
                title = line[10]
                img = line[21]
                self.books[bid] = [authors, year, title]
                self.ratings[bid] = list(map(int, line[-7:-2]))
                self.images[bid] = img
                
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
    def get_highest_rated_unvoted_book(self, num_books, early, late, genre):
        for bid in self.books:
            self.recommendations[bid] = self.get_rating(bid)
        temp = sorted(self.recommendations, key=self.recommendations.get, reverse=True)
        i = 0
        max_bid = []
        while i < len(temp) and len(max_bid) < num_books:
            if temp[i] not in self.voted_books:
                temp_book = self.get_book(temp[i])
                temp_year = temp_book[1]
                temp_genre = list(self.get_books_by_genre(int(genre)))
                if temp_year and temp_year >= int(early) and temp_year <= int(late):
                    if temp[i] in temp_genre:   
                        max_bid.append(temp[i])
            i += 1
        if (len(max_bid) == 0):
            max_bid.append(-1)
        return max_bid

