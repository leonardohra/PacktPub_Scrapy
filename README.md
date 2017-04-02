# PacktPub_Scrapy

Instalation

Easy way:

sudo apt-get install python3-pip python3-dev libssl-dev

sudo pip3 install -U pip beautifulsoup4 setuptools 

sudo pip3 install -U scrapy 

Note: If you try to install scrapy along with the others, it will give an error message, because it will not install the others first

Explaination:

There are 2 main files, a python script (url_books.py) and a Scrapy Spider (book_info_spider.py). I used python 3 for everything, so any "3" after some commands refer to that. url_books.py will use a library called "beautifulsoup", that needs to be installed before. You can install pip to install the library easily, the command to install pip on linux mint is 

sudo apt-get install python3-pip

Notice that I will install pip3, for python3. After this it's a good thing to update pip with the command 

pip3 install -U pip

THen install the library I said the script uses

pip3 install -U beautifulsoup4 

Then all that is left is to install the pre-requisites for scrapy. If you try to install scrapy the pip3 install, it will complain about not having setuptools, so install it first

pip3 install -U setuptools

Now if you try to install scrapy, it will complain about not having a Python.h (Python.h: No such file or directory), this is because we need to install Python headers, using the command

sudo apt-get install python3-dev

It might complain about not having the header file for openssl, so install the library to use this openssl

sudo apt-get install libssl-dev

Then you can finally install scrapy

sudo pip3 install -U scrapy


How to use it: 

Go to PacktPub's web site (https://www.packtpub.com) log in to your account, and go to your e-books (https://www.packtpub.com/account/my-ebooks). save this page as html, and put the html page on this project subdir called PacketPub/Support Files

Run the bash file that will do all the work, the result will be on books_info.csv

./run.sh
