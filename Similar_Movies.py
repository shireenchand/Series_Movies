import requests
from pprint import pprint
import texttable as tt

movies = []
dates = []
descs = []


api_key = ""
movie_name = input("Enter movie: ")

search_movie_base_url = "https://api.themoviedb.org/3/search/movie"
search_movie_url = f"{search_movie_base_url}?api_key={api_key}&query={movie_name}"

r1 = requests.get(search_movie_url)
response1 = r1.json()
results = response1['results']
movie_id = results[0]['id']

similar_movie_base_url = f"https://api.themoviedb.org/3/movie/{movie_id}/similar"
similar_movie_url = f"{similar_movie_base_url}?api_key={api_key}"

r2 = requests.get(similar_movie_url)
response2 = r2.json()
results = response2['results']


tab = tt.Texttable()
headings = ['Movie Name','Release Date','Description']
tab.header(headings)

for x in range(0,len(results)):
	movies.append(results[x]['original_title'])
	dates.append(results[x]['release_date'])
	descs.append(results[x]['overview'])


for row in zip(movies,dates,descs):
	tab.add_row(row)

s = tab.draw()
print(s)