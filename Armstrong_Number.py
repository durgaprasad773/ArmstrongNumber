a=input()
length = len(a)
first = int(a[0]) ** length
second = int(a[1]) ** length
third = int(a[2]) ** length

sum_of = first + second + third

if sum_of == int(a):
    print(True)
else:
    print(False)