KMP = []
k = 'a-z'
import re

def main():
    global k
    v=input("please input firstname-lastname")
    k=v
    split()
    return
def split():
    print(k)
    b=str(k)
    bb=b.split("-")
    ggg= str(bb)
    ggg= remove_lower(ggg)
    gggg=str(ggg)
    print (gggg)
    return k, ggg
def main():
    v = input("please input firstname-lastname")
    k=v
    split()
    return k
def split():
    print(k)
    b=str(k)
    bb=b.split("-")
    ggg= remove_lower(ggg)
    gggg=str(ggg)
    print(gggg)
    return k,ggg

main()
