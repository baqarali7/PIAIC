num = int (input("Enter Number to find its prime or not: "))

for i in range(2, num):
    if(num%i) == 0:
        print("Its not a prime number")
        break
    else:
        print("Its a prime number")
        break    






