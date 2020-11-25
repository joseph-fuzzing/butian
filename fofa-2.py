import base64
import requests
import json
import os
import sys
def search(key,size,page,email,tooken):
    url = "https://fofa.so/api/v1/search/all?email="+email+"&key="+tooken+"&qbase64=" + key + "&size=" + size + "&page=" + page+"&full=true"
    r=requests.get(url)
    for host in json.loads(r.text)['results']:
        host=(host[0])
        b = "https"
        result = b in host
        if result == True:
            print(host)
            f = open("url.txt", "a")
            f.write(host + "\n")
            f.close()
        else:
            print("http://" + host)
            f = open("url.txt", "a")
            f.write("http://" + host + "\n")
            f.close()

def main():
    email="22"
    tooken="22"
    str_key = input("输入关键词具体语法看佛法:").encode("utf-8")
    page = input("输入页码:")
    size = "10"
    key = (base64.b64encode(str_key))
    key = str(key, 'utf8')
    print(key)
    for page in range(0, int(page)):
        page = page + 1
        print("当前采集第" + str(page) + "页" + "本页" + str(size) + "条")
        search(str(key), str(size), str(page),str(email),str(tooken))
    name = input("保存列表名:")
    os.rename("url.txt", name)
    vg()
def vg():
    a = input("A继续，任意键退出:")
    if a=="A":
        main()
    else:
        pass
if __name__ == "__main__":
    print('''
    .d8888. d8888b. d88888b  .d8b.  d8888b. db   dD 
    88'千YP 88 `8D 88'    d8' `8b 88  `8D 88 ,8P' 
    `8bo.   88oodD' 88ooooo 88ooo88 88   88 88,8P   
      `Y8b. 88~~~   88~~~~~ 88~~~88 88   88 88`8b   
    db 晴8D 88     88.    88   88 88  .8D 88 `88. 
    `8888Y' 88      Y88888P YP   YP Y8888D' YP   YD 
    by===========嘿嘿
    ''')
    main()

