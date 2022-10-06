from unicodedata import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import requests
import ssl
from dotenv import load_dotenv
import os

load_dotenv()
# Variables de entorno
INSTAGRAM_USER = os.getenv("INSTAGRAM_USER")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")


PATH = "/Users/oktanait/Downloads/chromedriver"
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

time.sleep(4)
nothow = driver.find_element(
    "xpath", "//button[contains(text(), 'Not Now')]").click()
# turn on notif
time.sleep(4)
nothow2 = driver.find_element(
    "xpath", "//button[contains(text(), 'Not Now')]").click()


# searchbox
time.sleep(5)
searchbox1 = driver.find_element(
    "css selector", "svg[aria-label='Explore']").click()
time.sleep(5)
searchbox = driver.find_element("css selector", "input[placeholder='Search']")
searchbox.clear()
searchbox.send_keys("python4coding")
time.sleep(4)
searchbox.send_keys(Keys.ENTER)
time.sleep(4)
searchbox.send_keys(Keys.ENTER)
time.sleep(4)
# Scroll
scrolldown = driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
match = False
while (match == False):
    last_count = scrolldown
    time.sleep(3)
    scrolldown = driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
    if last_count == scrolldown:
        match = True

time.sleep(4)
posts = []
links = driver.find_elements("tag name", "a")
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
        posts.append(post)

print(posts)

# obteniendo videos
download_url = ''
for post in posts:
    driver.get(post)
    shortcode = driver.current_url.split("/")[-2]
    time.sleep(4)
    if driver.find_element("css selector", "img[style='object-fit: cover;']") is not None:
        download_url = driver.find_element(
            "css selector", "img[style='object-fit: cover;']").get_attribute('src')
        urllib.request.urlretrieve(download_url, '{}.jpg'.format(shortcode))
    else:
        download_url = driver.find_element(
            "css selector", "video[type='video/mp4']").get_attribute('src')
        urllib.request.urlretrieve(download_url, '{}.mp4'.format(shortcode))
    time.sleep(4)
