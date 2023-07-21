# File ecommerce.py - contains the logic of scraping the sample e-commerce site books.toscrape.com
#
# Created by @Shashwat Sharma
# 7/2023
# Copyright (c) 2023 Shashwat Sharma

# external libraries
from bs4 import BeautifulSoup
import pandas as pd

# utility module
import scraping_utils as sc

def scrape(selected_genre, path, file_name, save_choice):
    # scrape the home page to get the list of the genres and their links
    content = sc.get_content("http://books.toscrape.com/index.html")
    soup = BeautifulSoup(content, "html.parser")

    genres = soup.find("ul", {"class":"nav nav-list"}).find("li").find("ul").find_all("a")
    genres_labels = [] #stores the names of the genres
    genres_links = [] #stores the links of the different genres
    for genre in genres:
        genres_labels.append(genre.text.replace("\n","").strip().lower())
        genres_links.append(genre["href"])
    
    # after fetching the various genres and their links, we compare the user selected genre with the list of the genres and choose the appropriate URL
    selected_genre=selected_genre.lower()
    if selected_genre == "all" or selected_genre == "books":
        genre_url="https://books.toscrape.com/catalogue/category/books_1/index.html"
    else:
        try:
            genre_url="https://books.toscrape.com/"+genres_links[genres_labels.index(selected_genre)]
        except ValueError:
            raise ValueError("Invalid genre entered")
    
    content = sc.get_content(genre_url)
    soup = BeautifulSoup(content, "html.parser")
    
    # first page is always scraped regardless of genre
    products = soup.find_all("article", {"class":"product_pod"})
    l=[]
    for product in products:
        d={}
        d["Name"]=product.find("h3").find("a")["title"]
        d["Price"]=product.find("p", {"class":"price_color"}).text
        d["Avalibility"]=product.find("p", {"class":"instock availability"}).text.replace("\n","").strip()
        if product.find("p", {"class":"star-rating One"}) != None:
            d["Rating"]=1
        elif product.find("p", {"class":"star-rating Two"}) != None:
            d["Rating"]=2
        elif product.find("p", {"class":"star-rating Three"}) != None:
            d["Rating"]=3
        elif product.find("p", {"class":"star-rating Four"}) != None:
            d["Rating"]=4
        else:
            d["Rating"]=5
        l.append(d)

    # genre with single pages have only 1 <strong> (or bold) element in their <form> element n the format - "x results"
    # genre with multiple pages have only 3 <strong> (or bold) element in their <form> element in the format - "x results - showing y or z"
    res_count = soup.find("form", {"class":"form-horizontal"}).find_all("strong")
    if len(res_count) > 1:
        page_count=2 # starts from 2 since we already scraped the first page
         # the last 10 characters of the previous html contain "index.html" which is replaced by "page-" in order to create a base html
        base_url=genre_url[0:-10]+"page-"
        while True:
            content=sc.get_content(base_url,str(page_count),".html")
            soup = BeautifulSoup(content, "html.parser")
            products = soup.find_all("article", {"class":"product_pod"})
            for product in products:
                d={}
                d["Name"]=product.find("h3").find("a")["title"]
                d["Price"]=product.find("p", "price_color").text
                d["Avalibility"]=product.find("p", "instock availability").text.replace("\n","").strip()
                if product.find("p", {"class":"star-rating One"}) != None:
                    d["Rating"]=1
                elif product.find("p", {"class":"star-rating Two"}) != None:
                    d["Rating"]=2
                elif product.find("p", {"class":"star-rating Three"}) != None:
                    d["Rating"]=3
                elif product.find("p", {"class":"star-rating Four"}) != None:
                    d["Rating"]=4
                else:
                    d["Rating"]=5
                l.append(d)
            res_count = soup.find("form", {"class":"form-horizontal"}).find_all("strong")
            page_count += 1
            if int(res_count[0].text) == int(res_count[2].text):
                break

    # we pass the list of dictionaries to the pd.DataFrame() method in order to create a dataframe
    # which will then be stored in csv or xlsx format according to user choice
    df=pd.DataFrame(l)
    if save_choice==1:
        sc.save_data_xlsx(df, path, file_name)
    if save_choice==2:
        sc.save_data_csv(df, path, file_name)