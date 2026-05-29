# input
s = input("Enter sentence: ")
t = input("Enter target string: ")
# splitting list
s_list = s.split()
c = 0
# checking & output
if t in s_list:
    c = 1
else:
    c = 0
if c == 1:
    print("String Name Found")
else:
    print("String Not Found")