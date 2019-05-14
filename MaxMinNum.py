import random

arr = []

ran = int(input("Enter the range: "))

for x in range(ran):
  arr.append(random.randint(1 , 1000))


max = arr[0]
for i in range (1, ran):
    if arr[i] > max:
        max = arr[i]

min = arr[0]
for f in range (1, ran):
    if  min > arr[f]:
        min = arr[f]
print(arr)

strmax = str(max)
strmin = str(min)

print("Max value is : " + strmax)
print("Min value is : " + strmin)

val = arr[0]
for k in range(1, ran):
    val = val+arr[k]
avg = val/ran
stravg = str(avg)
print("Avrage of values is : " + stravg)