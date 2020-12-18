import cx_Oracle
import random

con = cx_Oracle.connect("musicapp/Shubham36@localhost:1522/orcl")
cur = con.cursor()
print(con.version)


num = random.randint(100,500)
print(num)