from bs4 import BeautifulSoup as soup
import requests

url = "https://www1.gogoanime.bid/category/naruto"
data_html = requests.get(url)
data_soup = soup(data_html.text,"html.parser")
episodes = data_soup.find('div',{'class':'anime_video_body'})

ep =episodes.find_all('a')
print (ep[-1]['ep_end'])
