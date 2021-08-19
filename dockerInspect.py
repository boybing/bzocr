# encoding: utf-8

import json
import traceback

def dockerformate(jsStr):

    restart="no" if(json.loads(jsStr)[0]["State"]["Restarting"]==False) else "always"
    imgname=json.loads(jsStr)[0]["Name"].replace("/","")
    image=json.loads(jsStr)[0]["Config"]["Image"]
    cmd=json.loads(jsStr)[0]["Config"]["Cmd"][0]
    network=json.loads(jsStr)[0]["HostConfig"]["NetworkMode"]
    volumn=json.loads(jsStr)[0]["Mounts"]
    workdir=json.loads(jsStr)[0]["Config"]["WorkingDir"]

    info=""
    info+="docker run --restart="+restart+" --name="+imgname+" --network="+network+" "
    if workdir:
        info+=" -w "+workdir
    try:
        for vname in volumn:
            v2=vname["Destination"]
            v1=vname["Source"]
            info+=" -v "+v1+":"+v2+" "
    except:
        info+=traceback.format_exc()
    try:
        for pname in json.loads(jsStr)[0]["NetworkSettings"]["Ports"]:
            port2=json.loads(jsStr)[0]["NetworkSettings"]["Ports"][pname][0]['HostPort']
            port1=pname.replace("/tcp","")
            info+=" -p "+port1+":"+port2+" "
    except:
        info+=traceback.format_exc()
    info+=" -t "+ image+" "+cmd+"\n"
    return info