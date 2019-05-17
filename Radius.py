r = int(input("Enter your radius to calculate area: "))
pie = 3.14
if r == 0:
    r = int(input("Enter radius value please: "))
    A = float(pie*(r*r))
    print(A)
else:
    A = float(pie*r)
    print(A)