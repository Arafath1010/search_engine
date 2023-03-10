# IMPORTS
subscription_key = "6c8086f863064921a6fd641e8ae1d3e7"
assert subscription_key

import requests


global text,simage,svideo

headers = {"Ocp-Apim-Subscription-Key": subscription_key}


#acces the news
def get_newses(search_term):
      search_url = "https://api.bing.microsoft.com/v7.0/news/search"
      news=[]
      params = {"q": search_term,"count":50, "textDecorations": True, "textFormat": "HTML"}
      response = requests.get(search_url, headers=headers, params=params)
      response.raise_for_status()
      search_results = response.json()
      
      for result in search_results["value"]:
            
            news.append((result["name"],result['url'],result['description']))
      return news





#access the all search images,video,text,links
def get_search(search_term):
      search_url = "https://api.bing.microsoft.com/v7.0/search"
      global text,simage,svideo
      text=[]
      simage=[]
      svideo=[]
      params = {"q": search_term,"count":100, "textDecorations": True, "textFormat": "HTML"}
      response = requests.get(search_url, headers=headers, params=params)
      response.raise_for_status()
      search_results = response.json()
      
      for result in search_results['webPages']['value']:
            try:
               text.append((result["name"],result['url'],result['snippet'],result["thumbnailUrl"]))
            except:
               text.append((result["name"],result['url'],result['snippet'],"https://store.ssebowa.org/static/img/logo.png"))
            
            
      try:
             for result in search_results['images']['value']:
                   
                   simage.append((result['thumbnailUrl'],result['hostPageUrl']))
      except:
            simage=[]

      try:
             for result in search_results['videos']['value']:
                   
                   svideo.append((result['thumbnailUrl'],result['hostPageUrl']))
      except:
            svideo=[]
      return text,simage,svideo





#for only image access
def get_images(search_term):
      search_url = "https://api.bing.microsoft.com/v7.0/images/search"
      image=[]
      params = {"q": search_term,"count":50, "textDecorations": True, "textFormat": "HTML"}
      response = requests.get(search_url, headers=headers, params=params)
      response.raise_for_status()
      search_results = response.json()
      
      for result in search_results["value"]:
            
            image.append((result["name"],result['thumbnailUrl'],result["contentUrl"],
                          result["hostPageUrl"]))
      return image

#for only video access
def get_videos(search_term):
      search_url = "https://api.bing.microsoft.com/v7.0/videos/search"
      video=[]
      params = {"q": search_term,"count":50, "textDecorations": True, "textFormat": "HTML"}
      response = requests.get(search_url, headers=headers, params=params)
      response.raise_for_status()
      search_results = response.json()
      
      for result in search_results["value"]:
            
            video.append((result["name"],result['thumbnailUrl'],
                          result["hostPageUrl"]))
      return video



# call the any function it will return results in list format
print(get_videos("car"))















