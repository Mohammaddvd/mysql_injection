from urllib.parse import ParseResultBytes
from webbrowser import get


from requests import *

def check_arg(url):
    if("http://" in url or "https://"):
        try:
            chk = get(url)
        except:
            return 0

        return 1