import pymysql as my
import os
from dotenv import load_dotenv

load_dotenv()

envhost = os.getenv('envhost')
envuser = os.getenv('envuser')
envpassword = os.getenv('envpassword')
envdb = os.getenv('envdb')
envcharset = os.getenv('envcharset')


def selectUsers(uid, upw):
    row = None
    connection = None
    try:
        connection = my.connect(host=envhost,
                                user=envuser,
                                password=envpassword,
                                database=envdb,
                                cursorclass=my.cursors.DictCursor
                                )
        cursor = connection.cursor()
        sql = '''SELECT * FROM userAccount WHERE userId=%s AND userPasswd=password(%s)'''
        cursor.execute(sql, (uid, upw))
        row = cursor.fetchone()
    except Exception as e:
        print('접속오류', e)
    finally:
        if connection:
            connection.close()
    return row