angle1 = int(input("Enter the angle : "))
angle2 = int(input("Enter the angle : "))
angle3 = int(input("Enter the angle : "))
if (angle1+angle2+angle3) == 180:
    s1 = int(input("Enter the side 1 : "))
    s2 = int(input("Enter the side 2 : "))
    s3 = int(input("Enter the side 3 : "))
    if(s1==s2==s3):
        print("Equa")
    elif ( (s1!=s2==s3) or (s1==s3!=s2) or( s1==s2!=s3)):
        print("iso")
    else:
        print("scal")
else:
    print("not valid ")