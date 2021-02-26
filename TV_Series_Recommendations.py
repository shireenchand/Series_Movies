import requests
from pprint import pprint
import texttable as tt

shows = []
dates = []
descs = []


api_key = ""
show_name = input("Enter name of the show: ")

search_show_base_url = "https://api.themoviedb.org/3/search/tv"
search_show_url = f"{search_show_base_url}?api_key={api_key}&query={show_name}"

r1 = requests.get(search_show_url)
response1 = r1.json()
results = response1['results']
show_id = results[0]['id']

recommend_show_base_url = f"https://api.themoviedb.org/3/tv/{show_id}/recommendations"
recommend_show_url = f"{recommend_show_base_url}?api_key={api_key}"

r2 = requests.get(recommend_show_url)
response2 = r2.json()
results = response2['results']


tab = tt.Texttable()
headings = ['Series Name','First Air Date','Description']
tab.header(headings)

for x in range(0,len(results)):
	shows.append(results[x]['original_name'])
	dates.append(results[x]['first_air_date'])
	descs.append(results[x]['overview'])


for row in zip(shows,dates,descs):
	tab.add_row(row)

s = tab.draw()
print(s)