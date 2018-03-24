import csv

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