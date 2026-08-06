limit = int(input())
target = int(input())
count = 0
total = 0
value = False
for i in range (limit+1):
    if i % 3 == 0:
        if target == i:
            value = True
        total = total + i
        count += 1
print(total)
print(count)
if value == True:
    print("Target found")
else:
    print("Target not found")

