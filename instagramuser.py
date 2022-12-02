from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import requests
import ssl
from dotenv import load_dotenv
import os

from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from PIL import Image
import sys
from sys import exit
from facebook_scraper import get_profile
from urllib.parse import urlparse, parse_qs
import numpy as np
import json


load_dotenv()
# Variables de entorno
INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")


PATH = "/Users/oktanait/Documents/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.instagram.com/")

ssl._create_default_https_context = ssl._create_unverified_context

# login
time.sleep(4)
username = driver.find_element("css selector", "input[name='username']")
password = driver.find_element("css selector", "input[name='password']")
username.clear()
password.clear()
username.send_keys(INSTAGRAM_USER)
password.send_keys(INSTAGRAM_PASSWORD)
login = driver.find_element("css selector", "button[type='submit']").click()

time.sleep(6)
nothow = driver.find_element(
    "xpath", "//button[contains(text(), 'Not Now')]").click()
# turn on notif
time.sleep(3)
nothow2 = driver.find_element(
    "xpath", "//button[contains(text(), 'Not Now')]").click()


# searchbox
time.sleep(3)
searchbox = driver.find_element("css selector", "input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("Jose Torres")
time.sleep(2)

#Logica para traer data de los primero 4 perfiles
arrayData = []
for publ in range(1,5):
    time.sleep(0.5)
    searchbox1 = driver.find_element(By.XPATH,"//div[contains(@class,'_aa61')]/div/div["+str(publ)+"]//div[contains(@class,'_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p _abcm')]")
    searchbox1 = searchbox1.text
    searchbox2 = driver.find_element(By.XPATH,"//div[contains(@class,'_aa61')]/div/div["+str(publ)+"]//div[contains(@class,'_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abb- _abcm')]")
    searchbox2 = searchbox2.text
    arrayData.append({'username':searchbox1, 'nombre':searchbox2, 'URL': "https://www.instagram.com/"+searchbox1})


res = json.dumps(arrayData)
print(res)

