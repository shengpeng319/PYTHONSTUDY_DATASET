
myinput = input("Please input the numbers split with comma: ")

mylist = myinput.split(',')

result = 0

for i in mylist:
    result = result + int(i)

print("The calculation result is ", result)