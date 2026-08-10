original = []
for i in range(3):
    original.append(int(input()))
alias = original
replace = int(input())
appendd = int(input())
alias[0] = replace
alias.append(appendd)
print(f"Original: {original}")
print(f"Alias: {alias}")
print(f"Shared Object: {original is alias}")