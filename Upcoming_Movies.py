import requests
from pprint import pprint
import texttable as tt
import datetime

pages = 1
movies = []
dates = []
descs = []
region = "US"
api_key = ""
base_url = "https://api.themoviedb.org/3/movie/upcoming"

for page in range(1,50):

	url = f"{base_url}?api_key={api_key}&page={pages}&region={region}"

	r = requests.get(url)

	response = r.json()
	results = response['results']

	tab = tt.Texttable()
	headings = ['Movie Name','Release Date','Description']
	tab.header(headings)


	now = datetime.datetime.now()


	for x in range(0,len(results)):
		changed = []
		changed.append(results[x]['release_date'].split("-"))
		change = datetime.datetime(int(changed[0][0]),int(changed[0][1]),int(changed[0][2]))
		if(change>now):
			movies.append(results[x]['original_title'])
			dates.append(results[x]['release_date'])
			descs.append(results[x]['overview'])

	pages+=1

for row in zip(movies,dates,descs):
	tab.add_row(row)

s = tab.draw()
print(s)