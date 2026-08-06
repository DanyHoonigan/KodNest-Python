limit = int(input("Enter the limit of the list:"))
list = []
total = 0
for i in range (limit):
    values = int(input("Enter the value of the list:"))
    list.append(values)
    total += i
highest = max(list)
lowest = min(list)
total = sum(list)
target = int(input("Enter the target value:"))
flag = False
for i in list:
    if target == i:
        flag = True
print(f"Highest Value in list is {highest}")
print(f"Lowest Value in list is {lowest}")
print(f"Total Value of list is {total}")
if flag:
    print("Target found")
else:
    print("Target not found")