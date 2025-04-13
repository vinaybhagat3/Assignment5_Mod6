#Created the dictionary of student data -> Name and Roll no.
stud_data = {'Alice':85, 'Jack':92, 'Rock':80}

a = input("Enter th student's name : ")

#Condition to check the student name is in dictionary then print their roll no.
if a in stud_data:
    x = stud_data.get(a)
    print(a,"'s marks: ",x)
else:
    print("Student not found.")
