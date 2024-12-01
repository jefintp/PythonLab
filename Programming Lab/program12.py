#Display first and last colours from a list of comma-separated colour names
colors = input("Enter a list of colors separated by commas: ")

colors_list = colors.split(",")
print("First: ", colors_list[0], "\nLast: ", colors_list[-1])
