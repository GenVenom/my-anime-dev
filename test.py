# from bs4 import BeautifulSoup as soup
# import requests
# from requests_html import HTMLSession


# url = "https://www1.gogoanime.bid/ninjala-episode-52"

# data_html = requests.get(url)

# data_soup = soup(data_html.text,"html.parser")

# link = data_soup.find("li",{"class":"dowloads"})

# ep_url =link.a['href']



# url = "https://gogohd.pro/download?id=MTk3NjA3&typesub=Gogoanime-SUB&title=Ars+no+Kyojuu+Episode+2"

# s = HTMLSession()
# s.browser

# def render_html():
#     r = s.get(url)
#     r.html.render(sleep=1)
#     anime = r.html.xpath('//*[@id="content-download"]',first= True)
    
#     dl_link = anime.find('div.dowload')
#     final_link = ""
#     for link in dl_link:
#         if 'gogodownload' in str(link.absolute_links):
#             final_link = link.absolute_links

#     print(final_link)


# render_html()


from selenium import webdriver

driver = webdriver.Chrome()
website = 'https://gogohd.pro/download?id=MTk3NjA3&typesub=Gogoanime-SUB&title=Ars+no+Kyojuu+Episode+2'

driver.get(website)
video = driver.find_element('xpath','//*[@id="content-download"]/div[1]/div[4]/a')
print(video.get_attribute('href'))