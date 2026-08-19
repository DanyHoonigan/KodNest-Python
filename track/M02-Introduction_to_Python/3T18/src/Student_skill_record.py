skills = []
# Read and store five skills
for i in range(5):
    skills.append(input())
# Convert the list into a tuple
tup = tuple(skills)
# Create the required slices
a = tup[0:3]
b = tup[-2:]
c = tup[::2]
d = tup[::-1]
# Display all required results
print(f"Skill Record: {tup}")
print(f"First Three: {a}")
print(f"Last Two: {b}")
print(f"Alternate Skills: {c}")
print(f"Reversed Skills: {d}")