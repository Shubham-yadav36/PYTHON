from cx import cx_Oracle
con = cx_Oracle.connect('Shubham/Shubham36@localhost')
cur = con.cursor()
print(cur.execute("Select * from emp"))
cur.close()
con.close()
