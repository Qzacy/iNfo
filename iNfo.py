#!/bin/python3
#by Qzacy

import subprocess 
import requests
from bs4 import BeautifulSoup

def scrapeInsta(soup_):
    i_data = []

    for meta in soup_.find_all(name="meta", attrs={"property": "og:description"}):
        i_data = meta["content"].split()
    followers = i_data[0]
    following = i_data[2]
    posts = i_data[4]

    print("\nUsername:  ", i_user)
    print("Posts:     ", posts)
    print("Followers: ", followers)
    print("Following: ", following)

if __name__ == "__main__":
    subprocess.call("clear")
    print ("Welcome to iNfo, coded by Qzacy.")
    i_user = input("Enter the username:\niNfo > ")
    i_url = "https://www.instagram.com/" + i_user
    i_page = requests.get(i_url)

    soup = BeautifulSoup(i_page.text, "html.parser")
    scrapeInsta(soup)