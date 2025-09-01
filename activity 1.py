medical_cause = input("Did you have a medical cause Y or N: ")
atten=int(input("Enter the attendance of the student: "))

if medical_cause == 'Y':
 print("The student is allowed to sit in the exam")
else:
 if atten >= 75:
        print("The student is allowed to sit in the exam")
 else:
        print("The student is not allowed to sit in the exam")
