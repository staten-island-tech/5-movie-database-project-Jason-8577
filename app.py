import json
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


Search = input("Enter movie name.")
Search == Search.lower()
def movie_search():
    found = 0
    for x in data:
        if Search.lower() in x['title'].lower():
            print(f"{x["title"].lower()}")
            a += 1
    if found == 0:
        print("The movie was not found")