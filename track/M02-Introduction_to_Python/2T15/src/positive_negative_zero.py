limit = int(input())

positive = 0
negative = 0
zero = 0
for i in range (limit+1):
    if i > 0 :
        positive += 1
    elif i<0:
        negative == 1
    else:
        zero += 1
print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zero: {zero}")