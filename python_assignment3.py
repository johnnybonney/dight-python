# -*- coding: utf-8 -*-
"""
John Bonney - 9.5.2017

Code to find marital status of PGA golfers

"""
import re
from urllib import request
from time import sleep

headers = {'user-agent': 'John Bonney (john.fbonney@gmail.com)'}
pages = ['https://www.pgatour.com/players/player.01810.html',
         'https://www.pgatour.com/players/player.22405.html',
         'https://www.pgatour.com/players/player.25364.html',
         'https://www.pgatour.com/players/player.29725.html',
         'https://www.pgatour.com/players/player.23325.html']
num = 0
for player in pages:
    page = request.urlopen(player)
    src = str(page.read())
    page.close()
    
    num += 1
    text_file = 'pga_child_birthdates' + str(num) + '.txt'
    with open(text_file, 'w') as file:
        file.write(src)
    
    with open(text_file, 'r') as file2:
        text = list(file2)[0]
        find_str = (
                '<p class="s-bottom-text">Residence</p>(.+)<p'
                ' class="s-bottom-text">Family</p>?')
        find_date = '\((\d+/\d+/\d+)\)'
        find_name = (
                '<meta name="title" content="(\w+ \w+)'
                ' - Official PGA TOUR Profile"/>')
        first_scrape = re.findall(find_str, text, re.DOTALL)
        date_scrape = re.findall(find_date, first_scrape[0], re.DOTALL)
        name = re.findall(find_name, text)[0]
        if date_scrape == []:
            print("No dates found for " + name + ".")
        else:
            print("Dates for " + name + ":", date_scrape)
            with open('pga_parsed.txt', 'a') as newfile:
                newfile.write(name + ": ")
                for date in date_scrape:
                    newfile.write(date + ", ")
                newfile.write("\n")
    sleep(3)
        
        
            
