subscription_key = "6c8086f863064921a6fd641e8ae1d3e7"
assert subscription_key

import requests





headers = {"Ocp-Apim-Subscription-Key": subscription_key}

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
