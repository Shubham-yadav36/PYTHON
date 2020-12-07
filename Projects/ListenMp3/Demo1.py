import cx_Oracle
import traceback

conn = None
try:
    conn = cx_Oracle.connect("musicapp/Shubham36@localhost:1522/orcl")
    print("Connected Succefully")
    print("DB Version", conn.version)
    print("DB User", conn.username)
except cx_Oracle.DatabaseError:
    print("DB Error")
    print(traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("Disconnected Successfully")
