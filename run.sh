#!/bin/bash

clear

dir="./PacketPub/Support Files/"
file="MyeBooks.html"

echo "First thing: Checking if your library's HTML file is on $dir"

if [ -f "$dir$file" ]
then 
	echo "File exists. Proceeding"
else
	echo "File doesn't exists. Please Log in your account on PacktPub, go to your eBooks and save that page as an HTML file on $dir"
	return 
fi 

echo "Second thing: Running ./url_books.py to get the url of all books that aren't free at all times, all output will be save in the file ./log"

python3 ./PacketPub/url_books.py > log

echo "URLs stored on file, time to scrape"

echo "Third thing: Running the spider to crawl in every site on the url file and save the info on ${dir}books_info.csv"

scrapy crawl booksinfospider >> log

echo "Process finished. If everything went right, the output file is ${dir}books_info.csv" 
