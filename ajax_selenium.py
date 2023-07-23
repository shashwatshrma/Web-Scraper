# File ajax_selenium.py - contains the logic for accessing and interacting a site with selenium and scraping it's data
# a very slow script which may take several minutes to execute
#
# Created by @Shashwat Sharma
# 7/2023
# Copyright (c) 2023 Shashwat Sharma

# external libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time
import random

# utility module
import scraping_utils as sc

def scrape(path, file_name, save_choice):

    # opens Chrome and loads the site
    driver=webdriver.Chrome()
    driver.get("https://www.scrapethissite.com/pages/ajax-javascript/")
    driver.implicitly_wait(5)

    # locates all the buttons that fetch the data upon clicking
    years=driver.find_elements(By.CLASS_NAME,"year-link")

    l=[]
    for year in years:
        year.click()
        # time delay in order to not overload the website
        # as well to wait for the data to load
        # randomness introduced in order to not be detected as a fixed interval may raise suspicion 
        time.sleep(random.randint(5,8)) 
        films=driver.find_elements(By.CLASS_NAME, "film")
        for film in films:
            d={}
            try:
                d["Title"]=film.find_element(By.CLASS_NAME, "film-title").text
                d["Nominations"]=film.find_element(By.CLASS_NAME, "film-nominations").text
                d["Awards"]=film.find_element(By.CLASS_NAME, "film-awards").text
            except:
                pass
            try:
                film.find_element(By.TAG_NAME, "i")
                d["Best Picture"]="Won"
            except:
                d["Best Picture"]=""
            l.append(d)

    # The opened Chrome window must be closed
    driver.quit()

    # we pass the list of dictionaries to the pd.DataFrame() method in order to create a dataframe
    # which will then be stored in csv or xlsx format according to user choice
    df=pd.DataFrame(l)
    if save_choice==1:
        sc.save_data_xlsx(df, path, file_name)
    if save_choice==2:
        sc.save_data_csv(df, path, file_name)