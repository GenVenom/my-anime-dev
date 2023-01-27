import re

from jikanpy import Jikan
jikan = Jikan()

class Anime:
    def __init__(self,mal_id,raw_anime_info = None):
        self.mal_id = mal_id
        self.raw_anime_info = raw_anime_info if raw_anime_info is not None else jikan.anime(mal_id)['data']
    

    def get_episodes(self):
        
        episodes = self.raw_anime_info['episodes']
        if episodes is not None:
            return episodes
        else:
            return 0
        
    def get_large_image(self):
        image = self.raw_anime_info['images']['jpg']['large_image_url']
        return image

    def get_synopsis(self):
        synopsis = self.raw_anime_info['synopsis']
        return synopsis

    def get_title(self):
        title = self.raw_anime_info['title']
        return title

    def sanitize_name(self):
        title=self.raw_anime_info['title']
        title = title.replace(' ','-')
        return title

    def get_rating (self):
        rating = self.raw_anime_info['rating']
        return rating

class Season:
    def __init__(self,mal_id,title,episodes,image_url,english_title,rating):
        self.mal_id = mal_id
        self.title = title
        self.episodes = episodes
        self.image_url = image_url
        self.english_title = english_title
        self.rating = rating
        

class Anime2:
    def __init__ (self,title,img_url,episodes=None,synopsis = None):
        self.title = title
        self.episodes = episodes
        self.img_url = img_url
        self.synopsis = synopsis
    
    def sanitize_name(self):
        title = re.sub(r'[^\w\s]', '', self.title).lower().replace(" ","-").strip()
        return title