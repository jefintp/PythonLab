n = int(input("Enter the number of key-value pairs: "))
dict = {}
for i  in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict[key] = value

print("User Dictionary:", dict)


myKeys = list(dict.keys())
asc=sorted(myKeys)
des=sorted(myKeys,reverse=True)
print(myKeys)

# Sorted Dictionary
print("Dictionary in ascending order:")
sd={i:dict[i] for i in asc}
print(sd)
print("Dictionary in descending order:")
sd1={i:dict[i] for i in des}
print(sd1)
