#from config import Config
from mysql import mysql.connector

def myslq_connect():
    myslq_config = {
        "user" : Config.MYSQL_USER,
        "password" : Config.MYSQL_PASS,
        "host" : Config.MYSQL_HOST
        "database" : Config.MYSLQ_DB
    }

    try:
        conn = mysql.connect(mysql_config)
        print(conn)

    except:
        print("bład")

mysql.connect()
