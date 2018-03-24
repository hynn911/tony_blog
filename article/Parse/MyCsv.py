import csv
from django.conf import settings
CSVdct = settings.CSVdct
Cmddct = settings.Cmddct

CSVdct = {}
Cmddct = {}

with open("D:\\work\\EXCEL\\CMD_para_info_simple.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cmd = row['命令']
        if (cmd not in CSVdct):
            CSVdct[cmd] = {}
            Cmddct[cmd] = row['命令名称']
        paradct = CSVdct[cmd]
        para = row['参数名称']
        if (para not in paradct):
            paradct[para] = row['中文意义']

def getnum(str1):
    outstr = ""
    str1 = str1.replace(";", "")
    strlst = str1.split(":")
    if (len(strlst) > 1):
        cmd = strlst[0]
        parastr = strlst[1].strip()
        if (cmd in Cmddct):
            outstr = outstr + Cmddct[cmd]
        else:
            outstr = outstr + strlst[0]
        if (len(parastr) > 0):
            outstr = outstr + ":"
            paralst = parastr.split(",")
            cdct = CSVdct[cmd]
            for p in paralst:
                vlst = p.split("=")
                if (len(vlst) > 1):
                    if (vlst[0] in cdct):
                        outstr = outstr+ cdct[vlst[0]] + "(" + vlst[1] + ")" + ","
                    else:
                        outstr = outstr + '"' + vlst[0] + ' "' + "(" + vlst[1] + ")" + ","
                else:
                    outstr = outstr + '"' + p + '"' + ","
            outstr = outstr[:len(outstr)-1]
    return outstr


if __name__ == '__main__':
    str1 = 'MOD LCK:IMSI="460025605024029",IC=FALSE,OC=FALSE,GPRSLOCK=FALSE;'
    print(getnum(str1))
