import pandas as pd

class movierec(object):

    def __init__(self):
        self.sheet = pd.read_csv("movies1.csv")
        self.profile = []

        self.list = []
        self.list = self.sheet[self.sheet.columns[2]].to_list()

        self.names = []
        self.names = self.sheet[self.sheet.columns[1]].to_list()


        self.dict = {}

        i = 0
        while i < len(self.sheet):
            title =self.sheet.iloc[i][1].lower().strip()
            title= title
            self.dict[self.sheet.iloc[i][1].lower()] = self.sheet.iloc[i][1:]

            i+=1


    def search(self,name):
        name = name.lower()
        name = name.strip()
        if name in self.dict:
            return True
        else:
            return False  
        #print(search("The Avengers"))

    def similar_names(self,title):
        possible_movies = []
        for arg in self.names:
            #arg = str(arg)
            if str(title.lower().strip()) in arg.lower().strip():
                possible_movies.append(arg)
        return possible_movies
    
    def add_movie(self, movie,rating):
        item = [movie, rating]
        self.profile.append(item)

    def comp(self,list):
            self.matches= []
            for value in list:
                if value not in self.metrics:
                    self.matches.append(0)
                else:
                    self.matches.append(1)
            return self.matches


        
    def find_weight(self,list):
        self.metrics = {}

        for value in list:
            if value[0] not in self.metrics:
                self.metrics[value[0]] = value[1]
            else:
                self.metrics[value[0]] += value[1]
        #print(metrics)
        for feature in self.metrics:
            self.metrics[feature] = self.metrics[feature]/(0.5*len((self.metrics)))
        #print(self.metrics)
    
    
    
    def find_movies(self):
        self.compare = {}
        for x in self.dict:
            self.compare[self.dict[x][0]] = str(self.dict[x][1]).split()
            #self.comp(str(self.dict[x][1]).split())]
        #print(self.compare)
        self.recommended = {}
        for movie in self.compare:
           # self.recommended = {}
            sum = 0
            for genre in self.compare[movie]:
                if genre in self.metrics:
                    sum += self.metrics[genre]* 1
                else:
                    sum -= 2
            #print(movie,sum)
            if sum > 0:
                self.recommended[movie] = sum
        self.recommended= sorted(self.recommended,key=lambda x:self.recommended[x],reverse=True)
        return  self.recommended

    def movie_picker(self):
        self.top_movies = []
        count = len(self.recommended) * 0.05
        count = int(count)
        #print(count)
        self.top_movies = [x for x in self.recommended]
        self.top_movies = self.top_movies[0:count]

        self.show_recs()
        return self.top_movies

    def show_recs(self):
        print("Based on your preferences, here are some movies I'm sure you'll love!:")
        self.top_movies = sorted(self.top_movies,key=lambda x: self.dict[x.lower()][2],reverse=True)  
        #print(self.top_movies)
        i = 5
        while i > -1:
            print(self.dict[self.top_movies[i].lower()],'\n')
            i-=1

        

    def prefrences(self):
        i = 0
        ratings = []
        output = {}
        while i < len(self.profile):
            ratings.append(self.profile[i][1])
        #    print(self.dict[self.profile[i][0]][1].split())
            i +=1
        self.list2 = []
        new = [str(n) for n in self.list]
        self.list = " ".join(new)
        self.list = self.list.split()
        for genre in self.list:
            if genre not in self.list2:
                self.list2.append(genre)
        self.list2.remove('nan')
        self.list2.remove('Movie')
        self.list2.remove('TV')
        #print(self.list2)
        picks = {}
        for movie in self.profile:
            picks[movie[0]] = self.list2
            list = []
            for genre in picks[movie[0]]:
                if genre in self.dict[movie[0]][1].split():
                    idk = [genre,1]
                    list.append(idk)
                    #print(1,genre)
                else:
                    idk = [genre,0]
                    list.append(idk)
                    #print(0,genre)
                #print(list)
            i = 0
            new_list = []
            while i< len(list):
                new_list += [[list[i][0],list[i][1]*movie[1]]]
                i+=1
            #print(new_list)
            output[movie[0]]=[new_list]
           # print(output)
        ik = []
        for movie in self.profile:
            
            for list in output[movie[0]]:
                for x in list:
                #   print(x[1])
                #print(x[1])
                    if x[1] > 0:
                        ik += [[x[0],x[1]]]
        self.find_weight(ik)
        self.find_movies()
        self.movie_picker()
        return ik

        #print(picks)



    

    def pick(self):
        i = 0
        while i < 3:
            self.item = []
            print("please select and rate a movie")

            movie = input().lower()
            movie = movie.strip()
            if self.search(movie) == False:

                while self.search(movie) == False:
                    print("Sorry, the movie you are lookiing for cannot be found in our database.\nPLease try again")
                    print("Maybe you're looking for one of these movies?")
                    for arg in self.similar_names(movie):
                        print(arg)

                    movie = input().lower()
                    movie = movie.strip()
                print("{} successfully added".format(movie))
                print("how would you rate this movie from 1-10")
                num = int(input())
                self.item = [movie,num]
                self.add_movie(movie,num)

                
            elif self.search(movie) == True:
                print("{} successfully added".format(movie))
                print("how would you rate this movie from 1-10")
                num = int(input())
                self.add_movie(movie,num)
            
            i+=1
        self.prefrences()
test = movierec()
test.pick()
#test.
