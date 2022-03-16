import requests
from bs4 import BeautifulSoup
import json
import pprint
def scrap_top_list():
    get_url=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/")
    soup=BeautifulSoup(get_url.text,"html.parser")
    # print(get_url.text)
    # print(soup.title.name)
    div=soup.find("div",class_="panel-body content_body allow-overflow")
    # print(tittle)
    tbody=div.find("table",class_="table")
    # print(tbody)
    trs=tbody.find_all("tr")
    # print(trs)
    top_movie_list=[]
    for tr in trs[1:]:
        rank=tr.find("td",class_="bold").get_text().strip()
        # print(rank)
        rank1=rank[:-1]
        # print(rank1)
        name=tr.find("a",class_="unstyled articleLink").get_text().split()
        # print(name)
        n=""
        for i in range(len(name)-1):
            n+=name[i]
        # print(n)
        year=name[-1][1:5]
        # print(year)
        rating=tr.find("span",class_="tMeterIcon tiny").get_text().strip()
        # print(rating)
        movie_link=tr.find("a",class_="unstyled articleLink")
        # print(movie_link)
        url=movie_link["href"]
        # print(url)
        movie_link_2=("https://www.rottentomatoes.com/")+url
        # print(movie_link_2)
        movie_details={}
        movie_details["rank"]=rank1
        movie_details["Name"]=n
        movie_details["Year"]=year
        movie_details["Rating"]=rating
        movie_details["MovieLink"]=movie_link_2
        top_movie_list.append(movie_details)
        # print(movie_details)
    # pprint.pprint(top_movie_list)
    with open("Task1.json","w") as read_content:
        json.dump(top_movie_list,read_content,indent=4)
    return top_movie_list
top_movie_list=scrap_top_list()



