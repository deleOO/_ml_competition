#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from download_gg_image import download_gg_image
import time 

#paths
path_image = 'C:/Users/ivand/OneDrive/Documenti/_ml_competition/images/'
path_drive = 'C:\Program Files (x86)\chromedriver.exe'

#load list of animal names from txt file
with open('A-Z_animals_1574.txt') as f:
    animals = f.readlines()

#clean the list of animal names
for i in range(len(animals)):
    animals[i] = animals[i][:-1]

#Opens up web driver and goes to Google Images accepting user conditions
driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe')
driver.get('https://images.google.com/')
box = driver.find_element_by_xpath('//*[@id="L2AGLb"]/div')
box.click()

#first search to make a test
box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
box.send_keys('test')
box.send_keys(Keys.ENTER)

#use download_gg_image function to download image looping the animal names list
for animal in animals:
    download_gg_image(driver, animal, 100, path_image)