# 	Roann Yanes
# 	Python Primer
# 	October 30, 2017

class _movie_database:

    def __init__(self):
        self.movies = {}
        self.users = {}
        self.ratings = {}
        self.images = {}
        self.recommendations = {}
	
    def load_movies(self, movie_file):
        for line in open(movie_file, "r"):
            self.movies[int(line.split("::")[0])] = line.strip().split("::")[1:]

    def get_movie(self, mid):
        if mid in self.movies:
            return (self.movies[mid])
        else:
            return None

    def get_movies(self):
        return [int(x) for x in list(self.movies)]

    def set_movie(self, mid, movies):
        self.movies[mid] = movies

    def delete_movie(self, mid):
        del self.movies[mid]

    def load_users(self, users_file):
        for line in open(users_file, "r"):
            info = line.strip().split("::")
            self.users[int(info[0])] = [info[1], int(info[2]), int(info[3]), info[4]]

    def get_user(self, uid):
        if uid in self.users:
            return (self.users[uid])
        else:
            return None
   
    def get_users(self):
        return [int(x) for x in list(self.users)]

    def set_user(self, uid, info):
        self.users[uid] = info

    def delete_user(self, uid):
        del self.users[uid]

    def load_ratings(self, ratings_file):
        for line in open(ratings_file, "r"):
            info = line.strip().split("::")
            if int(info[1]) not in self.ratings:
                self.ratings[int(info[1])] = {}
            self.ratings[int(info[1])].update({int(info[0]): float(info[2])})

    def get_rating(self, mid):
        if mid in self.ratings:
            return sum(self.ratings[mid].values())/len(self.ratings[mid])
        else:
            return 0

    def get_highest_rated_movie(self):
        highest = 0
        top = 0
        for mid in self.ratings:
            if self.get_rating(int(mid)) > highest:
                highest = self.get_rating(int(mid))
                top = mid
            elif self.get_rating(int(mid)) == highest and mid < top:
                highest = self.get_rating(int(mid))
                top = mid
        if highest > 0:
            return top
        else:
            return None
   
    def set_user_movie_rating(self, uid, mid, rating):
        self.ratings[mid].update({uid: rating})
 
    def get_user_movie_rating(self, uid, mid):
        return self.ratings[mid][uid]

    def delete_all_ratings(self):
        self.ratings = {}

    def load_images(self, image_file):
        for line in open(image_file, "r"):
            self.images[int(line.split("::")[0])] = line.strip().split("::")[2]

    def get_image(self, mid):
        if mid in self.images:
            return (self.images[mid])
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
