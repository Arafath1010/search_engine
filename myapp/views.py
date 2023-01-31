# IMPORTS
subscription_key = "6c8086f863064921a6fd641e8ae1d3e7"
assert subscription_key


#print(googletrans.LANGUAGES)
from googletrans import Translator
translator = Translator()

import requests


global text,simage,svideo

headers = {"Ocp-Apim-Subscription-Key": subscription_key}



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






def get_search(search_term,lang):
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
            if lang != 'en':
               t = translator.translate(result["name"],dest=lang).text

            else:
                t = result["name"]  
            try:
               
               text.append((t,result['url'],result['snippet'],result["thumbnailUrl"]))
            except:
               text.append((t,result['url'],result['snippet'],"https://store.ssebowa.org/static/img/logo.png"))
            
            
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























import os

from PIL import Image, ImageTk
import cv2,numpy
import os
 
import requests


from django.shortcuts import render ,redirect




global key
def visual(request):
      file = request.FILES["f"]
      f = file.read()
      np_array = numpy.asarray(bytearray(f),dtype="uint8")
      np_array = cv2.imdecode(np_array,cv2.IMREAD_COLOR)
      np_array = cv2.resize(np_array,(512,512))
      cv2.imwrite("s.jpg",np_array)
      img = {'file':open("s.jpg",'rb')}
      response = requests.post("http://127.0.0.1:8000",files=img)
      print(response.json())
      return render(request, 'visual.html',{'results':response.json()})


def home(request):

       return render(request, 'index.html')




def get_text(request):
            text = request.POST["t"]
            lang = 'en'#request.POST["l"]
            global key
            key = text
            text,simage,svideo = get_search(text,lang)
            #print(len(text),len(simage))
            return render(request,"base_results.html",{'results':text[0:10],'resultsimg':simage[0:4],
                                                       'resultvideo':svideo,"keyword":key,"active1":"active"})
def get_text_2(request):

            return render(request,"base_results.html",{'results':text[10:20],'resultsimg':simage[5:9],
                                                       'resultvideo':svideo,"keyword":key,"active2":"active"})
def get_text_3(request):

            return render(request,"base_results.html",{'results':text[20:30],'resultsimg':simage[10:14],
                                                       'resultvideo':svideo,"keyword":key,"active3":"active"})
def get_text_4(request):

            return render(request,"base_results.html",{'results':text[30:40],'resultsimg':simage[14:19],
                                                       'resultvideo':svideo,"keyword":key,"active4":"active"})
def get_text_5(request):

            return render(request,"base_results.html",{'results':text[40:50],'resultsimg':simage[19:23],
                                                       'resultvideo':svideo,"keyword":key,"active5":"active"})

def get_video(request):
            #text = request.POST["t"]

            video = get_videos(key)

            return render(request,"showvideo.html",{'results':video,"keyword":key})  

def get_img(request):
            #text = request.POST["t"]

            image = get_images(key)

            return render(request,"showimg.html",{'results':image,"keyword":key})

def get_news(request):
            #text = request.POST["t"]

            news = get_newses(key)

            return render(request,"shownews.html",{'results':news,"keyword":key})
