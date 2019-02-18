# Rhea Saldanha
# script to read reviews from www.rottentomatoes.com

# library imports
import webbrowser # default libary - to open webpage via script
import csv # defaut libabry - to save data in csv format
from requests import request # libabry to get webpage
from bs4 import BeautifulSoup # web scrapper library

def fetch_reviews(soup,url):
	# creating a csv file to store the reviews
	file = csv.writer(open(movieName+".csv", 'w'))
	file.writerow(['Author', 'Review'])
	pagination = soup.find('span',{'class':'pageInfo'})
	noOfReviewPage = int(pagination.text[10:])+1 # output of pagination = page 1 of 13 -- keep only last number
	for x in range(1, noOfReviewPage):
  		print("processing reviews on review page "+str(x))
  		newUrl = url+"?page="+str(x)
  		#print(new_url)
  		newPage = request('GET',newUrl);
  		newSoup = BeautifulSoup(newPage.text,'html.parser')
  		for review in newSoup.find_all("div", {"class": "review_table_row"}):
  			for reviewText in review.find_all("div", {"class":"the_review"}):
  				theReview =reviewText.text
  			for author in review.find_all("a", {"class":"articleLink"}):
  				theAuthor =author.text
			# writing each review to the csv file
  			file.writerow([theAuthor,theReview])

		


def webpage_url(url):
  page = request('GET',url)
  if page.status_code == 200 :

  	 #creating your beautiful soup object
  	 soup = BeautifulSoup(page.text, 'html.parser')
  	 fetch_reviews(soup,url)
  else:
  	print("Movie reviews not available")


# Request user to enter movie choice
movieName = input("Please Enter the Movie Name :").replace(" ", "_")
url = "https://www.rottentomatoes.com/m/"+movieName+"/reviews" #base page

webpage_url(url)





