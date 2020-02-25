from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time 
import random
import os
#import numpy as np

driver = webdriver.Chrome(os.path.join('ch', 'chromedriver.exe'))

dog_f = open("dog.txt", 'w')
not_dog_f = open("not_dog.txt", 'w')

#url_ = "https://www.google.com/search?sxsrf=ALeKk01nahAsCTLsNNyxY-ePrtI6FUl-Dg%3A1582526665063&ei=yXBTXsG8A4WC-QbMjK_wAQ&q=American+chameleon&oq=American+chameleon&gs_l=psy-ab.3..0i19l5j0i30i19l5.115464.115464..116894...0.2..0.122.122.0j1......0....2j1..gws-wiz.......0i71.LfRiW6juBno&ved=0ahUKEwiBxd-dy-nnAhUFQd4KHUzGCx4Q4dUDCAs&uact=5"
#url__ = "https://www.google.com/search?sxsrf=ALeKk01outnUzR2onEyUPbI5MjFzfyXEbA%3A1582527443606&ei=03NTXsLSJNLYhwOQ-5LIBw&q=beagle&oq=beagle&gs_l=psy-ab.3..0i67l2j0l8.497688.497688..498303...0.0..0.157.299.0j2......0....2j1..gws-wiz.......35i39j0i7i30j0i30.PlHl607h_dI&ved=0ahUKEwiCiP6QzunnAhVS7GEKHZC9BHkQ4dUDCAs&uact=5"

def get_dividend(url):
    html = requests.get(url).content
    #print(html)
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.select("div div div div span")
    info = str(tag)
    return ("개 품종" in info)

imagenet_labels = open('ImageNetLabels.txt').read().splitlines()

for label in imagenet_labels:
    driver.get('https://google.com')
    driver.find_element_by_name("q").send_keys(label + "\n")

    if get_dividend(driver.current_url):
        dog_f.write(label + "\n")
    else:
        not_dog_f.write(label + "\n")

    time.sleep(random.randint(1, 10))






#print(get_dividend(url_))
#print(get_dividend(url__))
