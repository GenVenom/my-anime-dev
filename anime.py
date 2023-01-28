import re

class Anime:
    def __init__ (self,title,img_url,episodes=None,synopsis = None):
        self.title = title
        self.episodes = episodes
        self.img_url = img_url
        self.synopsis = synopsis
    
    def sanitize_name(self):
        
        title =  re.sub(r'[^a-zA-Z0-9\s\-]', '', self.title).lower().replace(" ","-")
        return title