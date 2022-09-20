y=int(input("Enter Year"))
if(y%100==0):
    if(y%400==0):
        print("Leap Year")
    else:
        print("Normal Year")
else:
    if(y%4==0):
        print("Leap Year")
    else:
        print("Normal Year")