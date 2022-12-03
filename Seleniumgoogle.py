from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import requests
import ssl
from dotenv import load_dotenv
import os
import json

from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
from PIL import Image
import sys
from sys import exit
import json

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

driver = webdriver.Chrome('/Users/oktanait/Downloads/chromedriver', chrome_options=chrome_options)
#PATH = "/Users/oktanait/Downloads/chromedriver"

#driver = webdriver.Chrome(PATH)
name="giafar maldonado"
driver.get("https://www.google.com/search?q="+name)

ssl._create_default_https_context = ssl._create_unverified_context
time.sleep(4)
arrayData  = []
arrayData1 = []
for publ in range(1,8):
    searchbox2 = driver.find_element(By.XPATH,"//div[contains(@class,'v7W49e')]/div["+str(publ)+"]")
    searchbox2 = searchbox2.text
    arrayData.append(searchbox2)
    #print(searchbox2)

    #url
    if "Images" in searchbox2:
        searchbox1 = "No Posee URL"
        arrayData1.append(searchbox1)
        #print("imagen")
    else:
        searchbox1 = driver.find_element(By.XPATH,"//div[contains(@class,'v7W49e')]/div["+str(publ)+"]//div[contains(@class,'Z26q7c UK95Uc jGGQ5e')]/div/a").get_attribute('href')
        arrayData1.append(searchbox1)
        #print(searchbox1)
    
    time.sleep(1.5)

result = [{"URL": a, "Descripcion": b} for a, b in zip(arrayData1, arrayData)]
res = json.dumps(result)
print(res)
