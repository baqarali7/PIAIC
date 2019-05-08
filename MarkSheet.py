print("Welcome To Marksheet")
ColName = input("Enter College Name: ")
name = input("Enter Student Name: ")
RollNum = input("Enter Student Rollnumber: ")
print("------------------------------------------------------")
sub1 = int(input("Enter Subject 1 marks: "))
sub2 = int(input("Enter Subject 2 marks: "))
sub3 = int(input("Enter Subject 3 marks: "))
sub4 = int(input("Enter Subject 4 marks: "))
sub5 = int(input("Enter Subject 5 marks: "))
print("------------------------------------------------------")
total = sub1+sub2+sub3+sub4+sub5
percent = (total*100)/500

subStr1 = str(sub1)
subStr2 = str(sub2)
subStr3 = str(sub3)
subStr4 = str(sub4)
subStr5 = str(sub5)
percentStr = str(percent)

print("------------------------------------------------------")
print("College Name: " + ColName)
print("Student Name: " + name)
print("Roll Number: " + RollNum)
print("------------------------------------------------------")
print("Subject 1 Marks: " + subStr1)
print("Subject 2 Marks: " + subStr2)
print("Subject 3 Marks: " + subStr3)
print("Subject 4 Marks: " + subStr4)
print("Subject 5 Marks: " + subStr5)
print("------------------------------------------------------")

if sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100 or sub5 > 100:
    if(sub1 > 100):
        print("Invaild Subject Marks")
        print("Subject 1 marks: " +subStr1)
    elif(sub2 > 100):
        print("Invaild Subject Marks")
        print("Subject 2 marks: " +subStr2) 
    elif(sub3 > 100):
        print("Invaild Subject Marks")
        print("Subject 3 marks: " +subStr3)
    elif(sub4 > 100):
        print("Invaild Subject Marks")
        print("Subject 4 marks: " +subStr4)
    elif(sub5 > 100):
        print("Invaild Subject Marks")
        print("Subject 5 marks: " +subStr5)               

else:

    if percent >= 80 :
        if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
            print("You are Fail!")
            print("Your percentage is: " + percentStr) 
        else:
            print("You have got A+")
            print("Your percentage is: " + percentStr)

    elif percent >= 70 :
        if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
            print("You are Fail!")
            print("Your percentage is: " + percentStr) 
        else:    
            print("You have got A")
            print("Your percentage is: " + percentStr)

    elif percent >= 60 :
        if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
            print("You are Fail!")
            print("Your percentage is: " + percentStr) 
        else:    
            print("You have got B")
            print("Your percentage is: " + percentStr)

    elif  percent >= 50 :
        if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
            print("You are Fail!")
            print("Your percentage is: " + percentStr)
        else:     
            print("You have got C")
            print("Your percentage is: " + percentStr)

    elif percent >= 40 :
        if sub1 < 33 or sub2 < 33 or sub3 < 33 or sub4 < 33 or sub5 < 33:
            print("You are Fail!")
            print("Your percentage is: " + percentStr) 
        else:    
            print("You have got D")
            print("Your percentage is: " + percentStr)
    else:
        print("You are Fail!")
        print("Your percentage is: " + percentStr) 
           


