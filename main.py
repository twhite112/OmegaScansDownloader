from bs4 import BeautifulSoup as bs4
import requests
import urllib
import argparse
import wget
import os
import sys
import lxml

imagenum = 0
chapter_explain = '!under construction! Chapters You Wanna Scrape, Example: -C 12 [Gets Chapter 12], -C 1~4 [Gets Chapter 1, 2, 3, 4]'
name = ""
parsed_url = ''

def check_url(in_url):
    try:
        global parsed_url
        parsed_url = requests.get(in_url).text
    except:
        print("Wrong url, check your internet connection or the url")
        sys.exit()

def better_dirname(dirname):
    dirname = dirname.replace(' ', '-')
    dirname = dirname.replace(':', '')
    dirname = dirname.replace('*', '')
    dirname = dirname.replace('?', '')
    dirname = dirname.replace('"', '')
    dirname = dirname.replace("'", '')
    dirname = dirname.replace('|', '')
    dirname = dirname.replace('>', '')
    dirname = dirname.replace('<', '')
    dirname = dirname.lower()
    return dirname

def create_dir(html):
    soup = bs4(html, 'lxml')
    global name
    div = soup.find('div', {'class': 'allc'})
    soup2 = bs4(str(div), 'lxml')
    for a in soup2.find_all('a', href=True):
        name = a.text
    name = better_dirname(name)
    if not os.path.exists(name):
        os.makedirs(name)

def get_list(html):
    global imagenum
    soup = bs4(html, 'html.parser')
    #print("Initiating The Download of "+ soup.find('h3', {'class': 'entry-title'}))
    imgtags = soup.find_all('img', {'class': 'alignnone'})
    for image in imgtags:
        print("Downloading " + image['src'] + " 🐱‍🏍")
        get_image(image['src'])
        imagenum = imagenum + 1

def get_image(url):
    print()
    wget.download(url, out=name)

def initiate(url):
    check_url(url)
    create_dir(parsed_url)
    get_list(parsed_url)

# initiate(parsed_url)
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Download Manga from OmegaScans 🍌', usage='%(prog)s [options] URL', epilog='Thanks for using %(prog)s ✌')
        parser.add_argument('url', help='The URL to manga 🔥')
        args = parser.parse_args()
        initiate(args.url)
        print("Downloaded " + str(imagenum) + " images 🥳")
    except KeyboardInterrupt:
        print('\nKeyboard interrupt detected \nBye 😔')
