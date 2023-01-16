from bs4 import BeautifulSoup as soup
import requests
from selenium import webdriver
from animesearch import get_name_by_id
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')



async def get_stream_url(anime_id, ep_id):
    
    anime_name = get_name_by_id(anime_id)
    url = f"https://www1.gogoanime.bid/{anime_name}-episode-{ep_id+1}"
    
    data_html = requests.get(url)
    data_soup = soup(data_html.text,"html.parser")

    link = data_soup.find("li",{"class":"dowloads"})

    ep_url =link.a['href']
    url = ep_url

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    video = driver.find_element('xpath','//*[@id="content-download"]/div[1]/div[4]/a')
    
    return video.get_attribute('href')
   

