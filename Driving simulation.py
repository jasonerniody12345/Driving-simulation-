u = 0
Time_Velocity = 0
t = int(input("Time" ))
a = int(input("Aceleration" ))
s = int(input("Distance" ))
Speed_limit = 60

v = int(u + a*t)
d = (u*(t**2)/2)
for x in range(t+1):
    print("Duration",x,"Distance","*"*int((a*(x**2)/2)/10))

if v > 60:
   print("the person went over the speed limit","reached",v,"m/s")
else:
    print("the person did not reach the speed limit","Max speed was",v,"m/s")

if s >= d\
        :
     print("reach destination",d,"m/s")
else:
    print("did not reach the destination")


