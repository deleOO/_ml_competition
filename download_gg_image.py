#Imports Packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

def download_gg_image(driver, query, quantity, path_image):
    #get html pagess
    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input')
    box.send_keys(query)
    box.send_keys(Keys.ENTER)

    #Will keep scrolling down the webpage until it cannot scroll no more
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(2)
        new_height = driver.execute_script('return document.body.scrollHeight')
        try:
            driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            time.sleep(2)
        except:
            pass
        if new_height == last_height:
            break
        last_height = new_height


    #loop and take a screenshot of the images
    for i in range(quantity):
        try:
            driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+str(i)+']/a[1]/div[1]/img').screenshot(str(path_image)+str(query)+'_'+str(i)+'.png')
        except:
            pass