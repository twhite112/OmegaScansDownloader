from bs4 import BeautifulSoup as bs4
import requests
import urllib
import argparse
import wget
import os
import lxml

url = "https://omegascans.org/cheer-up-namjoo-chapter-1/"
imagenum = 0
name = ""

try:
    parsed_url = requests.get(url).text
except:
    print("Wrong url, check your internet connection or the url")
    sys.exit()

def initiate(html):
    create_dir(html)
    get_list(html)

def create_dir(html):
    soup = bs4(html, 'lxml')
    # h1s = soup.find('h1', {'class': 'entry-title'}).text
    # print(h1s)
    global name
    div = soup.find('div', {'class': 'allc'})
    soup2 = bs4(str(div), 'lxml')
    for a in soup2.find_all('a', href=True):
        name = a.text
    if not os.path.exists(name):
        os.makedirs(name)

def get_list(html):
    global imagenum
    soup = bs4(html, 'html.parser')
    soup
    #print("Initiating The Download of "+ soup.find('h3', {'class': 'entry-title'}))
    imgtags = soup.find_all('img', {'class': 'alignnone'})
    for image in imgtags:
        print("Downloading " + image['src'] + " 🐱‍🏍")
        get_image(image['src'])
        imagenum = imagenum + 1

def get_image(url):
    print()
    wget.download(url, out=name)

# initiate(parsed_url)
initiate(parsed_url)
print("Downloaded " + str(imagenum) + " images 🥳")