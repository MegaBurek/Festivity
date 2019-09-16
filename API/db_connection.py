from pymysql.cursors import DictCursor
import pymysql

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='festivity',
                             cursorclass=DictCursor)

