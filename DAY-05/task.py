#module
#m1
def findSquare(n):
    return n*n
#m2
def findcube(n):
    return n*n*n
#m3
def area(r):
    return 3.14*r*r
#m4
def rectangle(l,b):
    return l*b
#m5
def pos(n):
    if n > 0:
        return True
    else:
        return False
#m6
def neg(n):
    if n < 0:
        return True
    else:
        return False
#m7
def max(n,m):
    if n > m:
        return True
    else:
        return False
#m8
def login(username,password):
    if username == "Aarin" and password == 1234:
        return "Login Successfull...!!!"
#m9
def atmver(pin):
    if pin == 1202:
        return "Access Granted..!!"
#m10
def logout():
    return "Logout!!<3"