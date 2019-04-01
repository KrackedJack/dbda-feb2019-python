import cx_Oracle
con=cx_Oracle.connect('system/00001111@127.0.0.1/XE')
print(con.version)
print("[Connection successful]")
cur=con.cursor()

def insertDept():
    id=int(input("Please enter ID: "))
    name=input("Please enter name: ")
    sal=int(input("Please enter Salary: "))
    dept=input("Please enter Department: ")
    loc=input("Please enter Location: ")
    cur.execute("insert into mytables values(:id,:nm,:sa,:dept,:loc)",(id,name,sal,dept,loc))
    con.commit()

def deleteDept():
    dept=input("Please enter department: ")
    cur.execute("delete from mytables where dept= :id",(dept,))
    con.commit()

def updateDept():
    dept=input("Please enter the Department: ")
    name=input("please the Name to be updated: ")
    sal=int(input("Please enter updated salary: "))
    loc=input("please the Name to be updated: ")
    cur.execute("update mytables set name=:name,sal=:sal,loc=:loc where dept=:dept",(name,sal,loc,dept))
    con.commit()

def displayAllDept():
    cur.execute("Select * from mytables")
    all_rows=cur.fetchall()
    for row in all_rows:
        print("{0},{1},{2},{3},{4}".format(row[0],row[1],row[2],row[3],row[4]))

def displayDept():
    dept=input("Please enter the Department")
    cur.execute("Select * from mytables where dept=:dept",(dept,))
    all_rows=cur.fetchall()
    for row in all_rows:
        print("{0},{1},{2},{3},{4}".format(row[0],row[1],row[2],row[3],row[4]))

def displaydept():
    chck = input("Enter substring to search for in locations: ")
    cur.execute("select loc from mytables where loc like '%or%'")
    rows=cur.fetchall()
    if len(rows)==0: print("No records found.")
    else:
        for row in rows: 
            print(row[0])

            
while True:
    print("1. Insert Data.")
    print("2. Delete a particular Data.")
    print("3. Update Data.")
    print("4. Display Data.")
    print("5. Dispaly a particular Data.")
    print("6. Display a particular Department.")
    print("7. Exit.")
    c1=int(input("Enter choice: "))
    if c1==1:
        insertDept()
        print("Data inserted successfully.")
    elif c1==2:
        deleteDept()
        print("Data deleted successfully.")
    elif c1==3:
        updateDept()
        print("Data updated successfully.")
    elif c1==4:
        displayAllDept()
    elif c1==5:
        displayDept()
    elif c1==6:
        displaydept()
    elif c1==7:
        break
    else:
        print("Invlaid Input.")
        
            
       
   




