import hmac as hash
from re import search,M
from requests import get,post
from requests.utils import dict_from_cookiejar
from os import getenv
from hashlib import md5
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0"}
username = "xf20260003"
password=hash.new("FEqAm2pnA6Ed622VqmqLuSKdJ2WJplCT".encode(),"wKTM,071=x2ogeU(z5}p".encode(),"MD5").hexdigest()
cxk=md5()
cxk.update("********".encode())
password2=cxk.hexdigest()
r1=get("https://qoj.fzoi.top",headers=headers)
cookie1=dict_from_cookiejar(r1.cookies)
r2=get("https://qoj.fzoi.top/login",headers=headers,cookies=cookie1)
text=r2.text
jntm=search(r"_token : \"([A-Za-z0-9]+)\"",text,M)
if jntm==None:
    print("Error!")
    exit()
token=jntm.group(1)
r3=post("https://qoj.fzoi.top/login",cookies=cookie1,headers=headers,data={"username":username,"password":password,"ip":"","_token":token,"response":"","login":"","password2":password2})
cookie2=dict_from_cookiejar(r3.cookies)
if cookie2=={}:
    print("Something Wrong!")
    exit()
cookie1.update(cookie2)
get("https://qoj.fzoi.top/punch",headers=headers,cookies=cookie1)
print("OK!{}".format(username))
get("https://qoj.fzoi.top/logout",headers=headers,cookies=cookie1,params={"_token":token})
