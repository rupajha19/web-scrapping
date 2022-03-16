import json
import requests
from Task1 import top_movie_list
import os
from Task4 import scrap_movie_details
url=top_movie_list[0]["MovieLink"]
def scrape_new_movie_details(movie_details):
    for i in range(10):
        # print(movie_details)
        movie_id=""
        for id in movie_details[i][33:]:
            movie_id+=id
        # print(movie_id)
        file_name="/home/rupa/Desktop/web-scrapping/"+movie_id+".json"
        print(file_name)
        text=os.path.exists(file_name)
        # print(text)
        if text==True:
            with open(file_name,"r")as f:
                a=json.load(f)
            # return a
            # print(a)
        else:
            data=scrap_movie_details(url)
            with open(file_name,"w")as read_content:
                json.dump(data,read_content,indent=4)
            return data
    scrape_new_movie_details(url)
