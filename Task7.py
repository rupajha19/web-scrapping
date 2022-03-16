import json
def  analyse_movies_directors():
    file=open("Task5.json","r")
    file2=json.load(file)
    # print(h)
    list=[]
    for i in file2:
        if i["Director"]not in list:
            list.append(i["Director"])
            # print(i)
    dict8={}
    list9=[]
    for k in list:
        i=0
        count=0
        while i<len(file2):
            if k==file2[i]["Director"]:
                count+=1
            i+=1
        dict8.update({k:count})
    list.append(dict8)
    with open("Task7.json","w")as read_content:
        json.dump(dict8,read_content,indent=4)
    return dict8
analyse_movies_directors()
        