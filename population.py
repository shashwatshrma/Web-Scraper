# File population.py - contains the logic to scrape population data from worldometers.info
#
# Created by @Shashwat Sharma
# 7/2023
# Copyright (c) 2023 Shashwat Sharma

# external libraries
from bs4 import BeautifulSoup
import pandas as pd

# utility module
import scraping_utils as sc

def scrape(selected_region, path, file_name, save_choice):
    # a link is made on the user choice as the links follow the following format
    # https://www.worldometers.info/world-population/<selected_region>-population/ 
    c=sc.get_content("https://www.worldometers.info/world-population/", selected_region.lower(), "-population/")

    headings, rows=sc.get_table_contents(c, 1)

    df=sc.table_to_df(headings, rows)
    
    # the dataframe is stored in csv or xlsx format according to user choice
    if save_choice==1:
        sc.save_data_xlsx(df, path, file_name)
    if save_choice==2:
        sc.save_data_csv(df, path, file_name)