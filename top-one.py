list = [1,5,4,5,2,1,4,7,8,5,8,9,6,8,7,4,5,3,2,1,4,5]


def top_one(list):

    dic = {}

    for i in list:
        
        if i in dic.keys():
            dic[i] += 1 
        else:
            dic[i] = 1 

    return dic


print(top_one(list))