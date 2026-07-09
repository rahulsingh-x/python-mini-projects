students = {
  "Name" : "Rahul Singh",
  "Age" : "19",
  "Course" : "BCA"
}
print(" \n----------Current Details----------\n ")
print (students)

Update = input("\nWant to update the details? Yes/No\n")

if Update.strip().lower() == "yes":
  
  Select = input("\nWhat do you want to update? \n"
  "1. Name : \n"
  "2. Age : \n"
  "3. Course : \n"
  "4. Update All : \n"
  "5. Exit \n"
  "Enter your choice ")
  
  if Select.lower() in ["1","name"]:
    name = input("Enter the updated name : ")
    students["Name"] = name

  elif Select.lower() in ["2","age"]:
    age = input("Enter updated age : ")
    students["Age"] = age
  
  elif Select.lower() in ["3","course"]:
    course = input("Enter updated course : ")
    students["Course"] = course

  elif Select.lower() in ["4","update all"]:
    name = input("Enter the updated name : ")
    age = input("Enter updated age : ")
    course = input("Enter updated course : ")

    students["Name"] = name
    students["Age"] = age
    students["Course"] = course

  elif Select.lower() in ["5", "exit"]:
    print("Exiting")
    exit()

else:
  print("No changes were made ")
  exit()

print(" \n---------- Updated Details ----------\n ")

for key, value in students.items():
  print(key, ":", value)
 