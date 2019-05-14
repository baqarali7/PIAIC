import random

arr = []

ran = int(input("Enter the range: "))

for x in range(ran):
  arr.append(random.randint(1 , 1000))


max = arr[0]
for i in range (1, ran):
    if arr[i] > max:
        max = arr[i]
        index_max = i

min = arr[0]
for f in range (1, ran):
    if  min > arr[f]:
        min = arr[f]
        index_min = f
print(arr)

strmax = str(max)
strmin = str(min)
IndexStr_max = str (index_max)
IndexStr_min = str (index_min)

print("Max value is : " + strmax + " Index is : " + IndexStr_max)
print("Min value is : " + strmin + " Index is : " + IndexStr_min)

val = arr[0]
for k in range(1, ran):
    val = val+arr[k]
avg = val/ran
stravg = str(avg)
print("Avrage of values is : " + stravg)