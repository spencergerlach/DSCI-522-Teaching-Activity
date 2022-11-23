"This is a comment for the python file bar that changes the string SAM to its corresponding ascii characters"

name = "SAM"
bar = 0
for i in name:
    bar += ord(i)
print(bar)
