from bs4 import BeautifulSoup
import os
import sys

# Getting support file directory
sup_files_dir = os.path.dirname(os.path.realpath(sys.argv[0])) + "/Support Files/"
# Cleaning the urls.txt first
open(sup_files_dir + 'urls.txt', 'w').close()
# If the csv with books info exists, delete it, because maybe I'll use it
open(sup_files_dir + "books_info.csv", 'w').close()
# As I said, maybe I need to use it. And I will need to append
csv_books = open(sup_files_dir + "books_info.csv", 'a')
# Open the file that I've downloaded with the list of all my books
file = open(sup_files_dir + "MyeBooks.html", "r")
# Create a file that will store my urls
urls_file = open(sup_files_dir + 'urls.txt', 'w')
# Put the html file on a string
str_file = file.read()
# Closes the file
file.close()

# PacktPub really loves some exceptions
free_ebooks_exceptions = ['https://www.packtpub.com/game-development/getting-started-making-video-games']

# Parse the html string to a Soup file
soup = BeautifulSoup(str_file, "lxml")
# Get's the elements 'unseen'
unseen = soup.findAll("div", {"class" : "unseen"})

#for each one of them, get their url to the book's page and write it to the url file
for u in unseen:
	link = u.a['href']
	if "free-ebook" in link or link in free_ebooks_exceptions:
		name = u['title'][:-8] 
		csv_books.write(name + ";" + "Free eBook" + ";" + "0.00" + ";" + "" + ";" + link + ";" + "" + "\n")
	else:
		urls_file.write(link + '\n')

#close the url file
urls_file.close()
