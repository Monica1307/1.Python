lists=["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
class MultipleFunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        for fields in lists:
            print(fields)
    def OddEven():
        num=int(input("Enter the number"))
        if((num%2)==1):
            print(num, "is Odd number")
        else:
            print(num, "is Even number")
    def Eligible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        print("Your Gender:",gender)
        print("Your Age:",age)
        if(gender=="Male"):
            if(age>=21):
                print("ELigible")
            else:
                print("Not Eligible")
        elif(gender=="Female"):
            if(age>=18):
                print("Eligible")
            else:
                print("Not Eligible")
        else:
            print("Invalid Gender")
    def percentage():
        s1=int(input("Subject1="))
        s2=int(input("Subject2=")) 
        s3=int(input("Subject3="))
        s4=int(input("Subject4="))
        s5=int(input("Subject5="))
        total=s1+s2+s3+s4+s5
        print("Total:",total)
        percentage=(total/500)*100
        print("Percentage:",percentage)
    def triangle():
        height=int(input("Height:"))
        breadth=int(input("Breadth:"))
        area=(height*breadth)/2
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",area)
        height1 = int(input("Height1:"))
        height2 = int(input("Height2:"))
        breadth = int(input("Breadth:"))
        perimeter = height1 + height2 + breadth
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle:", perimeter)