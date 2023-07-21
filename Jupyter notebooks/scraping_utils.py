# File scraping_utils.py - contains utility functions which may be helpful when developing a webscraping script
#
# Created by @Shashwat Sharma
# 7/2023
# Copyright (c) 2023 Shashwat Sharma

# external libraries
import os
import time
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd

def get_content(basic_url="", input="", end_url="", time_delay=5):
    # time delay in order to not overload the website
    # randomness introduced in order to not be detected as a fixed interval may raise suspicion 
    time.sleep(random.randint(time_delay-2, time_delay+2))
    r=requests.get(basic_url+input.lower()+end_url)
    if(r.status_code!=200): #if status code is not 200 (OK), raise an exception
        raise ValueError("HTTP "+str(r.status_code)+" Error")
    return r.content

def get_table_contents(page_content, table_index=0):
    soup=BeautifulSoup(page_content, "html.parser")
    table=soup.find_all("table")[table_index]
    headings=table.find("thead").find_all("th")
    rows=table.find("tbody").find_all("tr")
    return headings, rows

def table_to_df(headings, rows):
    l=[]
    for table_row in rows:
        row_contents=table_row.find_all("td")
        d={}
        for heading, content in zip(headings, row_contents):
            d[heading.text]=content.text
        l.append(d)
    df=pd.DataFrame(l)
    return df

def save_data_xlsx(dataframe, dir, file_name, save_index=False):
    if dir=="" or file_name=="":
        raise ValueError("Invalid directory or file name entered")
    if not os.path.exists(dir): # if specified directory is not found, it is made
        os.makedirs(dir, exist_ok=True)
    if os.path.exists(dir+"/"+file_name+".xlsx"): # if an existing file is found, it is replaced 
        os.remove(dir+"/"+file_name+".xlsx")
    writer = pd.ExcelWriter(dir+"/"+file_name+".xlsx")
    dataframe.to_excel(writer, index=save_index)
    writer.close()
    

def save_data_csv(dataframe, dir, file_name, save_index=False):
    if dir=="" or file_name=="":
        raise ValueError("Invalid directory or file name entered")
    if not os.path.exists(dir): # if specified directory is not found, it is made
        os.makedirs(dir, exist_ok=True)
    if os.path.exists(dir+"/"+file_name+".csv"): # if an existing file is found, it is replaced
        os.remove(dir+"/"+file_name+".csv")
    dataframe.to_csv(dir+"/"+file_name+".csv", index=save_index)