from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
import os
import urllib.request
import random


# Scroll down to show more images
def scrollPages(num_of_pages, driver):
    SCROLL_PAUSE_TIME = 1
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")
    count = 0
    while True and (count < num_of_pages):
        count += 1
        # Scroll down to bottom
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        # mye4qd is the "show more results"  button
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height
        return num_of_pages, driver

#
def imageCrawl(name, limit, driver, num_of_pages):
    scrollPages(num_of_pages, driver)
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    count = 0
    for image in images:
        count = count + 1
        if count > limit:
            break
        try:
            image.click()
            time.sleep(random.randint(1, 3))
            # //*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img
            imgUrl = image.get_attribute('src')
            urllib.request.urlretrieve(
                imgUrl, 'image/' + str(name) + "/" + str(name) + "_" + str(count).zfill(3) + ".jpg")
            img_data = requests.get(imgUrl).content
            with open('image/' + str(name) + "_" + str(count).zfill(3) + '.jpg', 'wb') as handler:
                handler.write(img_data)
        except:
            pass
    driver.close()
