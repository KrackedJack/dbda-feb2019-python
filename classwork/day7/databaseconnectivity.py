import cx_Oracle
con=cx_Oracle.connect('system/dbda@127.0.0.1/XE')
print(con.version)
print("connection successfull")
cur=con.cursor()
id=111
name="yuri"
sal=2555.225
cur.execute("insert into mytable values(:id,:nm,:sa)",(id,name,sal))
id=100
name="gagrin"
sal=7000
cur.execute("insert into mytable values(:id,:nm,:sa)",(id,name,sal))
con.commit()
cur.execute("Select * from mytable")
#mydata1=cur.fetchone()
#print(mydata1[0],mydata1[1],mydata1[2])
all_rows=cur.fetchall()
for row in all_rows:
    print('{0}:{1}:{2}'.format(row[0],row[1],row[2]))

id=int(input("Please enter the id"))
sal=float(input("Enter the salary"))
cur.execute("update mytable set sal=:sal where id = :id",(sal,id))
cur.execute("Select * from mytable")
all_rows=cur.fetchall()
for row in all_rows:
    print('{0}:{1}:{2}'.format(row[0],row[1],row[2]))


id=int(input("Please enter the id"))
cur.execute("delete from mytable where id = :id",(id,))
cur.execute("Select * from mytable")
all_rows=cur.fetchall()
for row in all_rows:
    print('{0}:{1}:{2}'.format(row[0],row[1],row[2]))
con.close()
