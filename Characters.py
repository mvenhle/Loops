s = input("Input a string ")
d=l=0
for c in s:
    if c.isdigit():
        d += 1
    elif c.isalpha():
        l += 1
    else:
        pass

print("You have " + str(d) + " digits and have " + str(l) + " letters")
