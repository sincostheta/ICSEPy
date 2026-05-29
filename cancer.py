# initializing list
s = []
# initializing variable w/ integer 20
a = 20
# output
for i in range(a):
    s.append(input(f"Enter the {i+1}th student: "))
print("Original list: ", s)
print("Sorted list: ", sorted(s))