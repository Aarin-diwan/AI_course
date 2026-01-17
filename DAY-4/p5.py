# elif

a = [10,20,30]
b = [11,22,33,44,55,66,77]
c = [111,222,333]

if (len(a) > len(b)) and (len(a) > len(c)):
    print("list a is max")
elif (len(b) > len(a)) and (len(b) > len(c)):
    print("list b is max")
elif (len(c) > len(a)) and (len(c) > len(b)):
    print("list c is max")
else:
    print("all list are equal")