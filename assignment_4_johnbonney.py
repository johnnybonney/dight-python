"""
Write a brief summary explaining how you did the following task, and include
a link to your code. State what pattern you see in the files you saved. Are any
files missing, or is the pattern complete?

Write a function called `get_rnlp` that requests an arbitrary filename
(filename is an argument of the function) from `http:/reynoldsnlp.com/scrape/`
and saves the file in the local folder `scrape/`. (If you give the argument
"aa.html", it should return the html from
"http:/reynoldsnlp.com/scrape/aa.html".)

Write a function called `get_hrefs` that opens a file (filename is an argument
of the function), parses it using `BeautifulSoup` and returns a list of href
values for all <a> tags in the file.

The two functions above will be used for the following. Write a loop that will
iteratively request a url, parse it, extract the hrefs, and then do the same
thing with all of those hrefs. Begin with 'aa.html'.

There are many duplicates on the website. In your loop, be sure that you check
whether you have already saved a page before you request it.

IMPORTANT! Follow all ethical standards for scraping, especially the ~2-sec
pause between requests.
"""
import urllib.request as r
from bs4 import BeautifulSoup
import os
import time

os.chdir('C://Users//johnf//scrape')


def get_rnlp(filename):
    url = 'https://reynoldsnlp.com/scrape/' + filename
    r.urlretrieve(url, filename)


def get_hrefs(filename):
    with open(filename, "r") as g:
        soup = BeautifulSoup(g, 'html.parser')
        temp = soup.find_all('a')
        return [i.get('href') for i in temp]


headers = {'user-agent': 'John Bonney (john.fbonney@gmail.com)'}

file = 'aa.html'
link_list = [file]
get_rnlp(file)
for p in get_hrefs(file):
    q = p.split('/')[-1]
    link_list.append(q)

for link in link_list:
    get_rnlp(link)
    new_links = get_hrefs(link)
    time.sleep(2)
    for i in new_links:
        j = i.split("/")[-1]
        if j not in link_list:
            link_list.append(j)

link_list.sort()
