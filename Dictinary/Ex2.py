def defs_dic():
    i=0
    user_info = {}
    name , age ,fev_movie = input("enter you name,age,fev_movie :").split(",")
    user_info["name"] = name
    user_info["age"] = age
    user_info["fev_movie"] = fev_movie
    return  user_info


user = defs_dic();
print(user)
