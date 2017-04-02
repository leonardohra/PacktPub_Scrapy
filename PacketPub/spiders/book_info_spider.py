import scrapy
import os
import sys
from scrapy import Request


class BookInfoSpider(scrapy.Spider):
	name = "booksinfospider"
	# Getting support file directory
	global sup_files_dir 
	global log
	sup_files_dir = os.path.dirname(os.path.realpath(sys.argv[0])) + "/PacketPub/Support Files/"
	log = open("log", "a")
	
	def start_requests(self):
		with open(sup_files_dir + "urls.txt", "r") as urls:
			#log.write(' '.join(urls))
			for url in urls:
				yield Request(url, self.parse)

	def parse(self, response):
		category = response.xpath("//div[@data-product-category]/@data-product-category").extract_first()
		price = response.xpath("//div[@data-product-category]/@data-product-price").extract_first()
		title = response.xpath("//div[@data-product-category]/@data-product-title").extract_first()
		pages = response.xpath("//span[@itemprop='numberOfPages']/text()").extract_first()
		desc_textes = response.xpath("//div[@class='book-info-bottom-indetail-text']/p/text()").extract()
		description = ' '.join(str(elem) for elem in desc_textes)
		url = response.request.url

		books_info = open(sup_files_dir + "books_info.csv", "a")
		books_info.write(str(title) + ";" + str(category) + ";" + str(price) + ";" + str(pages) + ";" + str(url) + ";" + str(description) + '\n')
		books_info.close()