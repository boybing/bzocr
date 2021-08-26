# encoding: utf-8

import requests

def getTr():
    trls=["http://github.itzmx.com/1265578519/OpenTracker/master/tracker.txt","https://newtrackon.com/api/all","https://gitee.com/harvey520/www.yaozuopan.top/raw/master/blacklist.txt","https://cdn.jsdelivr.net/gh/ngosang/trackerslist/trackers_all.txt"]
    trtxt=""
    trFinal=""
    trResult=""
    for tr in trls:
        response=requests.get(tr)
        trResult+=tr+"下载成功！" if response.status_code==200 else tr+"下载失败！"
        trtxt+=response.text+"\n"

    for singleTr in [x for x in trtxt.split("\n") if x != ""]:
        if singleTr not in trFinal:
            trFinal+=singleTr+"\n"
    print(trFinal)
    print(trResult)
    return [trFinal,trResult]

if __name__ == '__main__':
    getTr()