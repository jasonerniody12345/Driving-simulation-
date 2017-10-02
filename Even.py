def throw():
    v= input("number:")
    if v.isdigit() is True:
        k = float(v)
        m= k%2
        if m== 0:
            print("alice won!")

        else:
            print("bob won!")

throw()