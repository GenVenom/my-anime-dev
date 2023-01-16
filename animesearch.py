from jikanpy import Jikan
from anime import Anime
jikan = Jikan()

def get_results(anime_name):
    results = []
    search_result = jikan.search('anime',anime_name)
    
    for i in range (10):
        results.append(search_result['data'][i]['titles'][0]['title'])
    
    return results

def get_season():
    results = []
    cur_season =  jikan.seasons(extension="now")
    
    for i in range(len(cur_season['data'])):
    
        cur_anime = cur_season['data'][i]
        mal_id =  cur_anime['mal_id']
        title = cur_anime['titles'][0]['title']
        episodes = cur_anime['episodes']
        image_url = cur_anime['images']['jpg']['image_url']
        english_title=  cur_anime['title_english']
        rating = cur_anime['rating']
        
        results.append(Anime(mal_id, title,episodes,image_url,english_title,rating))
    return results

def get_episodes(id):
    episodes = jikan.anime(id)['data']['episodes']
    if episodes is not None:
        return episodes
    else:
        return 0
        
def get_large_image(id):
    image = jikan.anime(id)['data']['images']['jpg']['large_image_url']
    return image

def get_info_by_id (id):
    synopsis = jikan.anime(id)['data']['synopsis']
    return synopsis

def get_name_by_id (id):
    title=jikan.anime(id)['data']['title']
    title = title.replace(' ','-')
    
    return title
def get_download_url(id):
    pass
