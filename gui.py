# File gui.py - implements all the different modules in an interactive application
# 
# Created by @Shashwat Sharma
# 7/2023
# Copyright (c) 2023 Shashwat Sharma

# external libraries
import customtkinter as ctk
import tkinter as tk
from tkinter.filedialog import askdirectory

# internal modules
import ecommerce
import population
import ajax_selenium
import ajax_requests


# function that is called when run button of "E-commerce Scraper" tab is clicked
# it calls the script defined in ecommerce.py and checks for exceptions 
# the status variable is updated accordingly
def scrape_ecommerce(genre, path, file_name, save_choice):
    try:
        global ecom_executed
        if ecom_executed == 0:
            ecommerce.scrape(genre, path, file_name, save_choice)
            ecom_executed=1
            status.set("Data saved as "+path+"/"+file_name)
        else:
            status.set("Script already ran, please reset")
    except ValueError as exc:
        status.set("Caught exception: "+repr(exc))


# function that is called when run button of "Population Scraper" tab is clicked
# it calls the script defined in population.py and checks for exceptions 
# the status variable is updated accordingly
def scrape_population(region, path, file_name, save_choice):
    try:
        global pop_executed
        if pop_executed == 0:
            population.scrape(region, path, file_name, save_choice)
            pop_executed=1
            status.set("Data saved as "+path+"/"+file_name)
        else:
            status.set("Script already ran, please reset")
    except ValueError as exc:
        status.set("Caught exception: "+repr(exc))


# function that is called when run button of "Ajax Scraper(Selenium)" tab is clicked
# it calls the script defined in ajax_selenium.py and checks for exceptions 
# the status variable is updated accordingly
def scrape_ajax_1(path, file_name, save_choice):
    try:
        global ajax_executed_1
        if ajax_executed_1 == 0:
            ajax_selenium.scrape(path, file_name, save_choice)
            ajax_executed_1=1
            status.set("Data saved as "+path+"/"+file_name)
        else:
            status.set("Script already ran, please reset")
    except ValueError as exc:
        status.set("Caught exception: "+repr(exc))


# function that is called when run button of "Ajax Scraper(Requests)" tab is clicked
# it calls the script defined in ajax_requests.py and checks for exceptions 
# the status variable is updated accordingly
def scrape_ajax_2(path, file_name, save_choice):
    try:
        global ajax_executed_2
        if ajax_executed_2 == 0:
            ajax_requests.scrape(path, file_name, save_choice)
            ajax_executed_2=1
            status.set("Data saved as "+path+"/"+file_name)
        else:
            status.set("Script already ran, please reset")
    except ValueError as exc:
        status.set("Caught exception: "+repr(exc))


# calls the askdirectory function defined in tkinter.filedialog
def pick_loc(path_var):
    path_var.set(askdirectory(title="Select directory"))


# following functions reset the tabs to their initial state  
def ecom_reset():
    path.set("")
    selected_genre.set("")
    file_name.set("")
    radio_var_1.set(2)
    global ecom_executed
    ecom_executed=0
    status.set("Reset")

def pop_reset():
    path_2.set("")
    selected_country.set("")
    file_name_2.set("")
    radio_var_2.set(2)
    global pop_executed
    pop_executed=0
    status.set("Reset")

def ajax_reset_1():
    path_3.set("")
    file_name_3.set("")
    radio_var_3.set(2)
    global ajax_executed_1
    ajax_executed_1=0
    status.set("Reset")

def ajax_reset_2():
    path_4.set("")
    selected_country.set("")
    file_name_4.set("")
    radio_var_4.set(2)
    global ajax_executed_2
    ajax_executed_2=0
    status.set("Reset")



# creating the window and setting the color theme, title and size
ctk.set_default_color_theme("green")
window=ctk.CTk()
window.title("Web Scraping and Generating Dataset Project")
window.geometry("650x550")
window.minsize(650, 550)



# adding widgets to the main window
title_text=ctk.CTkLabel(window, text="Web Scrapper Project", font=ctk.CTkFont("Robotto", size=27), height=50)

tabview=ctk.CTkTabview(window, height=420, width=500)
tabview.add("E-commerce Scraper")
tabview.add("Population Scraper")
tabview.add("AJAX Scraper (Selenium)")
tabview.add("AJAX Scraper (Requests)")

status=tk.StringVar(window, value="\tWelcome. Please select a web scraper and fill the details\t- Made by Shashwat Sharma")
status_field=ctk.CTkEntry(window, height=50, textvariable=status, state="disabled")


# adding widgets to the E-commerce tab
ecommerce_title=ctk.CTkLabel(tabview.tab("E-commerce Scraper"),
                             text="Book Ecommerce Website Scrapper",
                             font=ctk.CTkFont("Robotto", size=24), 
                             height=50)

# This variable ensures that the script is only ran once as to not send multiple requests to the websites
ecom_executed=0

selected_genre=tk.StringVar()
genre_entry=ctk.CTkEntry(tabview.tab("E-commerce Scraper"), textvariable=selected_genre , width=350)
genre_text=ctk.CTkLabel(tabview.tab("E-commerce Scraper"), text="Enter the genre of books to search:")

path=tk.StringVar(tabview.tab("E-commerce Scraper"))
location_entry=ctk.CTkEntry(tabview.tab("E-commerce Scraper"), textvariable=path, width=350)
location_text=ctk.CTkLabel(tabview.tab("E-commerce Scraper"), text="Directory to save the dataset into:")

file_name=tk.StringVar(tabview.tab("E-commerce Scraper"))
file_name_entry=ctk.CTkEntry(tabview.tab("E-commerce Scraper"), textvariable=file_name, width=150)
file_name_text=ctk.CTkLabel(tabview.tab("E-commerce Scraper"), text="Name of the file:")

pick_loc_button=ctk.CTkButton(tabview.tab("E-commerce Scraper"), text="Pick directory", command=lambda: pick_loc(path), width=100)
ecommerce_run_button=ctk.CTkButton(tabview.tab("E-commerce Scraper"),
                                   text="Get book data", 
                                   command=lambda: scrape_ecommerce(selected_genre.get(), path.get(), file_name.get(), radio_var_1.get()))

ecommerce_reset_button=ctk.CTkButton(tabview.tab("E-commerce Scraper"), text="Reset", command=ecom_reset)

radio_var_1=tk.IntVar(tabview.tab("E-commerce Scraper"), 2)
ecom_save_choice_1=ctk.CTkRadioButton(tabview.tab("E-commerce Scraper"), text="Save as excel file", variable=radio_var_1, value=1)
ecom_save_choice_2=ctk.CTkRadioButton(tabview.tab("E-commerce Scraper"), text="Save as csv file", variable=radio_var_1, value=2)

ecom_credits=ctk.CTkLabel(tabview.tab("E-commerce Scraper"), text="Data taken from: http://books.toscrape.com/", text_color="grey")


# Population tab is structured similar to the E-commerce tab
population_title=ctk.CTkLabel(tabview.tab("Population Scraper"), 
                              text="Population data Scrapper", 
                              font=ctk.CTkFont("Robotto", size=24), 
                              height=50)

pop_executed=0

selected_country=tk.StringVar()
country_entry=ctk.CTkEntry(tabview.tab("Population Scraper"), textvariable=selected_country, width=350)
country_text=ctk.CTkLabel(tabview.tab("Population Scraper"), text="Enter the country:")

path_2=tk.StringVar(tabview.tab("Population Scraper"))
location_entry_2=ctk.CTkEntry(tabview.tab("Population Scraper"), textvariable=path_2, width=350)
location_text_2=ctk.CTkLabel(tabview.tab("Population Scraper"), text="Directory to save the dataset into:")

file_name_2=tk.StringVar(tabview.tab("Population Scraper"))
file_name_entry_2=ctk.CTkEntry(tabview.tab("Population Scraper"), textvariable=file_name_2, width=150)
file_name_text_2=ctk.CTkLabel(tabview.tab("Population Scraper"), text="Name of the file:")

pick_loc_button_2=ctk.CTkButton(tabview.tab("Population Scraper"), text="Pick directory", command=lambda: pick_loc(path_2), width=100)
population_run_button=ctk.CTkButton(tabview.tab("Population Scraper"),
                                    text="Get data",
                                    command=lambda: scrape_population(country_entry.get(), path_2.get(), file_name_2.get(), radio_var_2.get()))

population_reset_button=ctk.CTkButton(tabview.tab("Population Scraper"), text="Reset", command=pop_reset)

radio_var_2=tk.IntVar(tabview.tab("Population Scraper"), 2)
pop_save_choice_1=ctk.CTkRadioButton(tabview.tab("Population Scraper"), text="Save as excel file", variable=radio_var_2, value=1)
pop_save_choice_2=ctk.CTkRadioButton(tabview.tab("Population Scraper"), text="Save as csv file", variable=radio_var_2, value=2)

pop_credits=ctk.CTkLabel(tabview.tab("Population Scraper"), text="Data taken from: https://www.worldometers.info/", text_color="grey")


# Ajax Scraper tabs are structured similar to the E-commerce tab
# Ajax web scrapers do not except a parameter other than the save location and file name as it scrapes the info for all the years
ajax_title_1=ctk.CTkLabel(tabview.tab("AJAX Scraper (Selenium)"),
                          text="AJAX Scraper using Selenium",
                          font=ctk.CTkFont("Robotto", size=24),
                          height=50)

ajax_executed_1=0

ajax_text=ctk.CTkLabel(tabview.tab("AJAX Scraper (Selenium)"), text="Scraping the data of:")
ajax_url=ctk.CTkLabel(tabview.tab("AJAX Scraper (Selenium)"), text="https://www.scrapethissite.com/pages/ajax-javascript/")

path_3=tk.StringVar(tabview.tab("AJAX Scraper (Selenium)"))
location_entry_3=ctk.CTkEntry(tabview.tab("AJAX Scraper (Selenium)"), textvariable=path_3, width=350)
location_text_3=ctk.CTkLabel(tabview.tab("AJAX Scraper (Selenium)"), text="Directory to save the dataset into:")

file_name_3=tk.StringVar(tabview.tab("AJAX Scraper (Selenium)"))
file_name_entry_3=ctk.CTkEntry(tabview.tab("AJAX Scraper (Selenium)"), textvariable=file_name_3, width=150)
file_name_text_3=ctk.CTkLabel(tabview.tab("AJAX Scraper (Selenium)"), text="Name of the file:")

pick_loc_button_3=ctk.CTkButton(tabview.tab("AJAX Scraper (Selenium)"), text="Pick directory", command=lambda: pick_loc(path_3), width=100)
ajax_run_button=ctk.CTkButton(tabview.tab("AJAX Scraper (Selenium)"), 
                              text="Get book data", 
                              command=lambda: scrape_ajax_1(path_3.get(), file_name_3.get(), radio_var_3.get()))

ajax_reset_button=ctk.CTkButton(tabview.tab("AJAX Scraper (Selenium)"), text="Reset", command=ajax_reset_1)

radio_var_3=tk.IntVar(tabview.tab("AJAX Scraper (Selenium)"), 2)
ajax_save_choice_1=ctk.CTkRadioButton(tabview.tab("AJAX Scraper (Selenium)"), text="Save as excel file", variable=radio_var_1, value=1)
ajax_save_choice_2=ctk.CTkRadioButton(tabview.tab("AJAX Scraper (Selenium)"), text="Save as csv file", variable=radio_var_1, value=2)


# This web scraper uses a workaround by taking the data from the data source url instead of interacting with the webpage 
ajax_title_2=ctk.CTkLabel(tabview.tab("AJAX Scraper (Requests)"), 
                          text="AJAX Scraper using Requests", 
                          font=ctk.CTkFont("Robotto", size=24), height=50)

ajax_executed_2=0

ajax_text_2=ctk.CTkLabel(tabview.tab("AJAX Scraper (Requests)"), text="Scraping the data of:")
ajax_url_2=ctk.CTkLabel(tabview.tab("AJAX Scraper (Requests)"), text="https://www.scrapethissite.com/pages/ajax-javascript/")

path_4=tk.StringVar(tabview.tab("AJAX Scraper (Requests)"))
location_entry_4=ctk.CTkEntry(tabview.tab("AJAX Scraper (Requests)"), textvariable=path_4, width=350)
location_text_4=ctk.CTkLabel(tabview.tab("AJAX Scraper (Requests)"), text="Directory to save the dataset into:")

file_name_4=tk.StringVar(tabview.tab("AJAX Scraper (Requests)"))
file_name_entry_4=ctk.CTkEntry(tabview.tab("AJAX Scraper (Requests)"), textvariable=file_name_4, width=150)
file_name_text_4=ctk.CTkLabel(tabview.tab("AJAX Scraper (Requests)"), text="Name of the file:")

pick_loc_button_4=ctk.CTkButton(tabview.tab("AJAX Scraper (Requests)"), text="Pick directory", command=lambda: pick_loc(path_4), width=100)
ajax_run_button_2=ctk.CTkButton(tabview.tab("AJAX Scraper (Requests)"), text="Get book data", command=lambda: scrape_ajax_2(path_4.get(), file_name_4.get(), radio_var_4.get()))
ajax_reset_button_2=ctk.CTkButton(tabview.tab("AJAX Scraper (Requests)"), text="Reset", command=ajax_reset_2)

radio_var_4=tk.IntVar(tabview.tab("AJAX Scraper (Requests)"), 2)
ajax_save_choice_2_1=ctk.CTkRadioButton(tabview.tab("AJAX Scraper (Requests)"), text="Save as excel file", variable=radio_var_1, value=1)
ajax_save_choice_2_2=ctk.CTkRadioButton(tabview.tab("AJAX Scraper (Requests)"), text="Save as csv file", variable=radio_var_1, value=2)



# managing the layout and placing widgets in the window
# the coordinates for place() method were decided mostly by experiment
title_text.pack()

ecommerce_title.pack()
genre_text.place(x=10, y=60)
genre_entry.place(x=10, y=90)
location_text.place(x=10, y=130)
location_entry.place(x=10, y=160)
pick_loc_button.place(x=370, y=160)
file_name_text.place(x=10, y=200)
file_name_entry.place(x=110, y=200)
ecom_save_choice_1.place(x=20, y=250)
ecom_save_choice_2.place(x=200, y=250)
ecommerce_run_button.place(x=100, y=300)
ecommerce_reset_button.place(x=250, y=300)
ecom_credits.place(x=0, y=340)



population_title.pack()
country_text.place(x=10, y=60)
country_entry.place(x=10, y=90)
location_text_2.place(x=10, y=130)
location_entry_2.place(x=10, y=160)
pick_loc_button_2.place(x=370, y=160)
file_name_text_2.place(x=10, y=200)
file_name_entry_2.place(x=110, y=200)
pop_save_choice_1.place(x=20, y=250)
pop_save_choice_2.place(x=200, y=250)
population_run_button.place(x=100, y=300)
population_reset_button.place(x=250, y=300)
pop_credits.place(x=0, y=340)



ajax_title_1.pack()
ajax_text.place(x=10, y=60)
ajax_url.place(x=10, y=90)
location_text_3.place(x=10, y=130)
location_entry_3.place(x=10, y=160)
pick_loc_button_3.place(x=370, y=160)
file_name_text_3.place(x=10, y=200)
file_name_entry_3.place(x=110, y=200)
ajax_save_choice_1.place(x=20, y=250)
ajax_save_choice_2.place(x=200, y=250)
ajax_run_button.place(x=100, y=300)
ajax_reset_button.place(x=250, y=300)



ajax_title_2.pack()
ajax_text_2.place(x=10, y=60)
ajax_url_2.place(x=10, y=90)
location_text_4.place(x=10, y=130)
location_entry_4.place(x=10, y=160)
pick_loc_button_4.place(x=370, y=160)
file_name_text_4.place(x=10, y=200)
file_name_entry_4.place(x=110, y=200)
ajax_save_choice_2_1.place(x=20, y=250)
ajax_save_choice_2_2.place(x=200, y=250)
ajax_run_button_2.place(x=100, y=300)
ajax_reset_button_2.place(x=250, y=300)



tabview.pack()
status_field.pack(fill="x", side="bottom")

window.mainloop()