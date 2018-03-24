from django.db.models.expressions import connection
from article.models import CmdinfoHwhss

def dictfetchall(cursor):
    cols = [col[0] for col in cursor.description]
    return [
        dict(zip(cols,row))
        for row in cursor.fetchall()
    ]

def geCmdStr(str1):
    outstr = ""
    str1 = str1.replace(";", "")
    strlst = str1.split(":")
    if (len(strlst) > 1):
        cmd = strlst[0]
        parastr = strlst[1].strip()

        post = CmdinfoHwhss.objects.get(cmd=cmd)
        outstr = outstr + post.cmd_name
        dictparalst = post.param.split("||")
        paranamelst = post.param_name.split("||")
        if (len(parastr) > 0):
            outstr = outstr + ":"
            paralst = parastr.split(",")
            # cdct = CSVdct[cmd]
            for p in paralst:
                vlst = p.split("=")
                if (len(vlst) > 1):
                    try:
                        pi = dictparalst.index(vlst[0])
                        outstr = outstr + paranamelst[pi] + "(" + vlst[1] + ")" + ","
                    except:
                        outstr = outstr + '"' + vlst[0] + ' "' + "(" + vlst[1] + ")" + ","
                else:
                    outstr = outstr + '"' + p + '"' + ","
            outstr = outstr[:len(outstr)-1]
    return outstr

def getCmdDetail( cmdDict):
    val = {}
    for cmd in cmdDict:
        cmdStr = cmd['MML_COMMAND']
        val[cmd['STARTTIME']] = geCmdStr(cmdStr)
    return val


def getHwssLogDetail( msisdn_no, begMnth, endMnth):
    with connection.cursor() as cursor:
        cursor.execute("call getuser2(%s,%s,%s)", (msisdn_no, begMnth, endMnth,))
        # val = cursor.fetchall()
        val = dictfetchall(cursor)
        for post in val:
            post["cmdparse"] = geCmdStr(post['MML_COMMAND'])
    return val
if __name__ == '__main__':
    str1 = 'MOD LCK:IMSI="460025605024029",IC=FALSE,OC=FALSE,GPRSLOCK=FALSE;'
    print(geCmdStr(str1))