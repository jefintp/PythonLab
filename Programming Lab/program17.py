numbers = []
n=int(input("Enter the size of the list: "))
for i in range(n):
    numbers.append(int(input(f"numbers[{i}]: ")))

newlist = [x for x in numbers if x % 2 != 0]
print(newlist)
