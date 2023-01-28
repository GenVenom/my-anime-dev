# from bs4 import BeautifulSoup as soup
# import requests

# url = "https://www1.gogoanime.bid/category/naruto"
# data_html = requests.get(url)
# data_soup = soup(data_html.text,"html.parser")
# episodes = data_soup.find('div',{'class':'anime_video_body'})

# ep =episodes.find_all('a')
# print (ep[-1]['ep_end'])

# anime_info = data_soup.find('div',{'class':'anime_info_body_bg'})
# title = anime_info.h1.text

# print(title)

import re
title = "delicious-partyprecure-movie-yume-miru-okosama-lunch"
title =  re.sub(r'[^a-zA-Z0-9\s\-]', '', title).lower().replace(" ","-")

print(title)