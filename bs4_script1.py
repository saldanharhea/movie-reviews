from urllib2 import urlopen
from bs4 import BeautifulSoup
import webbrowser
import csv

movie_name = raw_input("name of ur movie : ").replace(" ", "_")

print (movie_name)
html = urlopen("https://www.rottentomatoes.com/m/"+movie_name+"/reviews")
bsObj = BeautifulSoup(html.read() ,"lxml");
#webbrowser.open_new("https://www.rottentomatoes.com/m/"+movie_name+"/reviews")

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['Name', 'Link'])

for review in bsObj.findAll("div", {"class": "review_table_row"}):
	for review_txt in review.findAll("div", {"class":"the_review"}):
		print(review_txt.text)
		f.writerow([i, review_txt.text])
	
