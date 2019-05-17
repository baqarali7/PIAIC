Date1 = int(input("Enter date 1: "))

if Date1 > 31 or Date1 <= 0:
    print("Please Enter valide date")
    Date1 = int(input("Enter date1 again: "))

Date2 = int(input("Enter date 2: "))

if Date2 > 31 or Date2 < Date1 or Date2 <= 0:
    print("Please Enter valide date")
    Date2 = int(input("Enter date2 again: "))

StrDate1 = str(Date1)
StrDate2 = str(Date2)

Diff = Date2 - Date1

StrDiff = str(Diff)
print("Number of Days between " + StrDate1 + " and " + StrDate2 + " are " + StrDiff)
