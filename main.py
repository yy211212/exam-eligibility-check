medical_cause=input("did you have a medical cause Y or Z: ")
atten = int(input("enter the attendence of student: "))
if medical_cause=='Y':
    print("you are allowed")
else:
    if atten>=75:
        print ("Allowed")
    else:
        print("not allowed")