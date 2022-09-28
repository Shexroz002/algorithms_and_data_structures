
def foctaryal(n):
    if n == 1:
        return 1
    else:
        return  n*foctaryal(n-1)

print(foctaryal(7))


