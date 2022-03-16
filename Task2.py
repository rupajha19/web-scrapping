import requests
import json
from bs4 import BeautifulSoup
import pprint
from Task1 import top_movie_list
def group_by_year(movies):
    years=[]
    # a={}
    for i in movies:
        year=i["Year"]
        if year not in years:
            years.append(year) 
        # print(year)
    movie_dict={i:[]for i in years}
    for i in movies:
        # name=i
        year=i["Year"]
        for x in movie_dict:
            if str(x)==str(year):
                movie_dict[x].append([i])
    with open("Task2.json","w") as read_content:
        json.dump(movie_dict,read_content,indent=4)
        return movie_dict
# print(group_by_year(top_movie_list))

group_by_year(top_movie_list)
dec_arg=group_by_year(top_movie_list)





