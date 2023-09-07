import requests
import json
from jarvis.config.configuration import news_api

file_path='jarvis\\database\\allnews.json'

def news_url(para):
    url= 'https://newsapi.org/v2/top-headlines'

    news = requests.get(url,params=para).text
    news_dict = json.loads(news)
    # with open(file_path,'r') as file:
    #     existing_data = json.load(file)
    # existing_data.append(news_dict)
    with open(file_path, 'w') as file:
    # Storing data into json file
        json.dump(news_dict, file)
    print(news)
    articles = news_dict['articles']
    
    return articles

def get_news():
    categories = ['business','entertainment','general','health','science','sports','technology']
    # counries = [''] you can later add counries as well 
    print(categories)
    # https://newsapi.org/docs/endpoints/everything Please reffer this for improve news functionalities 
    para = {
        'apiKey':news_api,
        'pageSize':10,
        'country':'in'
    }
    articles = news_url(para)

    return articles
def getNewsUrl():
    return 'http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=ae5ccbe2006a4debbe6424d7e4b569ec'


