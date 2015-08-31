import os
import sys
import json
from tkinter import *
from bs4 import BeautifulSoup
import requests
import tkinter

class Scraper(object):
    def __init__(self, url):
        print(url)
        self.url = url

    def getReviews(self):
        page = requests.get("http://www.gamespot.com" + self.url + "/reviews")
        data = page.text
        soup = BeautifulSoup(data)

        results = soup.find_all(class_="userReview-list__item")

        # Clear content area and get new content
        text.delete("1.0", END)
        for item in results:
            # get each review
            title = item.find(class_="media-title").find('a').string
            content = item.find(class_="userReview-list__deck").get_text()
            rating = item.find(class_="media-well--review-user").find('strong').string

            # insert content
            text.insert(INSERT, "TITLE: ")
            text.insert(INSERT, title)
            text.insert(INSERT, "\n")
            text.insert(INSERT, "RATING: " + rating + "\n")
            text.insert(INSERT, "REVIEW: ")
            text.insert(INSERT, content)
            text.insert(INSERT, "\n\n")

            print(item.find(class_="media-title").find('a').string)

        print("Done")

def ok():
    # os.system('python walmartscraper.py "' + self.e.get() + '"')
    query = e.get()
    url = "http://www.gamespot.com/search/?q=" + query
    r = requests.get(url)
    data = r.text
    soup = BeautifulSoup(data)
    results = soup.get_text()
    results = soup.find("ul", class_='search-results')
    link = results.find('a')
    #print(link.get('href'))

    scraper = Scraper(link.get('href'))
    scraper.getReviews()

root = Tk()
root.title('Game Reviews')
img = tkinter.PhotoImage(file='icon-games.gif')
root.tk.call('wm', 'iconphoto', root._w, img)

e = Entry(root)
e.pack(padx=5)
b = Button(root, text="Search", command=ok)
b.pack(pady=5)

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill=Y)

text = Text(root, yscrollcommand = scrollbar.set, wrap="word")
text.insert(END, "Search for game reviews")

text.pack(side = LEFT, fill = BOTH)

scrollbar.config(command = text.yview)

#root.wait_window(root)
mainloop()