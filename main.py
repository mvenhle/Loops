numbers = range(0, 5000)
count_odd = 0
count_even = 0
for x in numbers:
    if not x % 2:
        count_even +=1
    else:
        count_odd +=1

print("Number of even numbers is " + str(count_even))
print("Number of odd numbers is " + str(count_odd))
