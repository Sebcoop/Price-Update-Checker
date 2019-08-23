from bs4 import BeautifulSoup
import requests
import smtplib


# method to check when a certain 
def checkPrice():

	# url of the page we want to scrape
	URL = ""

	# add header
	# find user agent by searching 'my user agent' on google
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

	# get the page
	page = requests.get(URL, headers=headers)
	soup = BeautifulSoup(page.content, "lxml")

	# use Dev Tools to find certain html element
	title = soup.find(id="productTitle").get_text().strip()
	price = soup.find(id="price_inside_buybox").get_text().strip()

	# cast and convert the price to represent a float without £ sign
	converted_price = float(price[1:6])

	# print the product and price
	print("PRODUCT: ", title.strip())
	print("COST: £", converted_price)

	# price we want to buy product for
	requiredPrice = 100

	# provide logic for when we should send the email
	if converted_price <= requiredPrice:
		sendEmail(str(requiredPrice))
	else:
		print("Price not changed")


# method to send an email
# p = requiredPrice
def sendEmail(price):
	content = "The price of your product has dropped to £{}, buy product now!".format(price)
	mail = smtplib.SMTP("smtp.gmail.com", 587)
	mail.ehlo()
	mail.starttls()
	# enter email and password of gmail account
	mail.login("email", "password")
	# enter fromemail, recipient
	mail.sendmail("fromemail","recipient", content)
	print("EMAIL SENT")
	mail.close()


# main
# could add logic in here, using the time lib, to run this script after a given amount of time
checkPrice()
