import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

Movies = [
  {
    "title": "The Silent Call",
    "year": 1961,
    "cast": ["Gail Russell", "David McLean"],
    "genres": ["Drama"],
    "href": "The_Silent_Call",
    "extract": "The Silent Call is a 1961 American drama film directed by John A. Bushelman and written by Tom Maruzzi. The film stars Gail Russell, David McLean, Roger Mobley, Roscoe Ates, Milton Parsons and Dal McKennon.",
    "thumbnail": "https://upload.wikimedia.org/wikipedia/en/7/79/The_Silent_Call_poster.jpg",
    "thumbnail_width": 255,
    "thumbnail_height": 390
  },
  {
    "title": "The Sinister Urge",
    "year": 1961,
    "cast": ["Kenne Duncan", "Jean Fontaine"],
    "genres": ["Drama", "Crime"],
    "href": "The_Sinister_Urge_(film)",
    "extract": "The Sinister Urge is a 1960 crime drama film that was written, directed and co-produced by Ed Wood. It starred Kenne Duncan, Duke Moore, Dino Fantini, Jean Fontaine, Harvey Dunn and Conrad Brooks.",
    "thumbnail": "https://upload.wikimedia.org/wikipedia/en/1/10/The_Sinister_Urge.jpg",
    "thumbnail_width": 260,
    "thumbnail_height": 384
  },
  {
    "title": "The Sins of Rachel Cade",
    "year": 1961,
    "cast": ["Angie Dickinson", "Peter Finch", "Roger Moore"],
    "genres": ["Drama"],
    "href": "The_Sins_of_Rachel_Cade",
    "extract": "The Sins of Rachel Cade is a 1961 drama film directed by Gordon Douglas and starring Angie Dickinson in the title role as well as Peter Finch and Roger Moore.",
    "thumbnail": "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Thesinsofrachelcade.JPG/320px-Thesinsofrachelcade.JPG",
    "thumbnail_width": 320,
    "thumbnail_height": 245
  }
]
for index, item in enumerate(Movies):
    print(index, ":", item["title"])