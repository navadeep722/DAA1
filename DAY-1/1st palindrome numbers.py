a = ["wel", "aba", "madam", "string"]
r = " "
for i in a:
    if i == i[::-1]:  
        r = i
        break  
if r != " ":  
    print(r)
else:
    print("None")
