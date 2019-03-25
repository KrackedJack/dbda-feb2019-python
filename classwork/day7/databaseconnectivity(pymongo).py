from pymongo import MongoClient
client=MongoClient('localhost:27017')
print("connection done")

db=client.EmployeeData
employeeId=int(input("Enter the id"))
employeeName=input("Enter the Name")
employeeAge=int(input("Enter the Age"))
employeeCountry=input("Enter the Country")
db.employees.insert_one(
    {
     "id": employeeId,
          "name":employeeName,
     "age": employeeAge,
     "country":employeeCountry})

try:
    empCol=db.employees.find()
    print('\n All data from EmployeeData Database\n')
    for emp in empCol:
        print(emp)
        
except Exception as e:
    print(str(e))
try:
    criteria = int(input('\nEnter id to update\n'))
    name = input('\nEnter name to update\n')
    age = int(input('\nEnter age to update\n'))
    country = input('\nEnter country to update\n')

    db.employees.update_one({"id":criteria},{"$set": {
                 "name":name,
                 "age":age,
                 "country":country}})
    
    print("Records updated Successfully")
except Exception as e:
    print(str(e))

try:
    criteria = int(input('\nEnter id to delete\n'))
    db.employees.delete_many({"id":criteria})
    print('\nDeletion successful')
except Exception as e:
    print(str(e))
