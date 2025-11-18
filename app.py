import json
from re import search
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

""" for index, item in enumerate(data):
    print(index, ":", item["title"]) """


""" given_year = int(input("input the year."))
for movies in data:
    if movies['year'] > given_year:
        print(movies['title'], movies['year']) """


""" given_year = int(input("Input the smaller year."))
set_year = int(input("Input the larger year."))
for movies in data:
    if movies['year'] > given_year and movies['year'] < set_year:
        print(movies['title'], movies['year']) """


""" given_year = int(input("Input the year."))
for movies in data:
    if movies['year'] == given_year:
        print(movies['title'], movies['year']) """


""" def search_movies(movies, search):
    search = search.lower()
    results = []
    for movies in data:
        if search in movies["title"].lower():
            results.append(movies['title'])
    return results
Search = input("What movie would you like to watch?")
results = search_movies(movies, Search)
print(results) """


def search(movies, genre):
    genre = genre.lower()
    results = []
    for movies in data:
        if genre in movies["genres"].lower():
            results.append(movies['genres'])
    return results
Search = input("What movie genre would you like to view?")
results = search(movies, Search)
print(results)