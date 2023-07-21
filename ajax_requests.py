# File ajax_requests.py - instead of interacting with the site using AJAX, 
# this file contains the logic to get the json hosted on another URL from which the main webpage fetches the data from 
# the aim of this module is to compare the speeds of web scraping through selenium and through requests library
#
# Created by @Shashwat Sharma
# 7/2023
# Copyright (c) 2023 Shashwat Sharma

# external libraries
import requests
import time
import pandas as pd

# utility module
import scraping_utils as sc

def scrape(path, file_name, save_choice):
    l=[]
    for year in range(2010, 2016):
        time.sleep(5)
        r=requests.get("https://www.scrapethissite.com/pages/ajax-javascript/?ajax=true&year="+str(year))
        l.extend(r.json())
    
    # we pass the list of dictionaries to the pd.DataFrame() method in order to create a dataframe
    # which will then be stored in csv or xlsx format according to user choice
    df=pd.DataFrame(l)
    if save_choice==1:
        sc.save_data_xlsx(df, path, file_name)
    if save_choice==2:
        sc.save_data_csv(df, path, file_name)