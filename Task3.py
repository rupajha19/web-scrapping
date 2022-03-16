import requests
import json
from bs4 import BeautifulSoup
import pprint
from Task1 import top_movie_list
from Task2 import dec_arg
def group_by_decade(movies):
    movie_dec={}
    list1=[]
    for index in movies:#years
        mod=int(index)%10 #mod=3
        print(index)

        decade=int(index)-mod #decade 1973-mod=1970
        if decade not in list1:
            list1.append(decade)#it is creating list of decades
        print(list1)
    list1.sort()
    for i in list1:
        movie_dec[i]=[]
    # print(movie_dec)
    for i in movie_dec:
        dec10=i+9 #dec10=e.g 1959 or i= e.g 1950
        for x in movies:
            if int(x)<=dec10 and int(x)>=i: #dec10=e.g 1959 or i=e.g 1950
                for v in movies[x]:
                    movie_dec[i].append(v)
    with open("Task3.json","w") as  read_content:
        json.dump(movie_dec,read_content,indent=4)           
    return movie_dec
group_by_decade(dec_arg)
print(group_by_decade(dec_arg))

