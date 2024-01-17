import socket
import numpy as np
import pymysql
from dotenv import load_dotenv
import os


load_dotenv()
db =None
cur = None
envhost = os.getenv('envhost')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')
db = pymysql.connect(host=envhost, user=envuser, password=envpassword, db=envdb, charset=envcharset)

cnt = 0

while True:
    data_size = 1024
    rline=[]
    txtv=''
    sqlv=''
    if lc > 50:
        for i in range(0,lc):
                sqlv = sqlv + "'" + rline[i] + "',"
                txtv = txtv + 'd' +str('{0:03}'.format(i+1)) + ','
        if rline[3] == "SYSTEM":
            pass
        else:
            try:
                cur = db.cursor()
                sql = f"INSERT INTO logger.inoutT " +"("+ txtv +")"+ f" VALUES "+"("+ sqlv +")"
                cur.execute(sql)
                db.commit()
                cnt += 1
                print(cnt)
            except pymysql.err.InternalError as e:
                code, msg = e.args
                pass
    else:
        pass