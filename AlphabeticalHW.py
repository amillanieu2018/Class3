statement = "azcbobobegghakl"
longest = ""
temp = ""

for i in statement:
    if len(temp) == 0:
        temp += i
        continue
    if i >= temp[-1]:
        temp += i
    else:
        longest = temp
        temp = i
print(longest)