class classLibrary():
     def subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech processing")
        print("Natural Language processing")

     def OddEven(num):        
        if(num%2==0):
            message="Even Number"
        else:
            message="Odd Number"        
        return message


     def Eligible(Gender,Age):        
        if(Gender=="Male"):
            if(Age<21):
                message="NOT ELIGIBLE"
            else:
                message="ELIGIBLE"
        else:
            if(Age<21):
                message="NOT ELIGIBLE"
            else:
                message="ELIGIBLE"
        return message        

     def Percentage(list):
        Total=sum(list)
        Average=Total/len(list)
        print("Total :", Total)
        print("Average :", Average)
        return  Total , Average

     def triangle():
        Height=int(input("Height:"))
        Breadth=int(input("Breadth:"))
        print("Area of formula: (Height*Breadth)/2")
        Area=(Height*Breadth)/2
        print("Area of Triangle :", Area)
        Height1=int(input("Height1:"))
        Height2=int(input("Height2:"))
        Breadth=int(input("Breadth:"))
        print("Perimeter formula: (Height1+Height2+Breadth)")
        Perimeter=(Height1+Height2+Breadth)
        print("Perimeter of Triangle :", Perimeter)
        return Area, Perimeter

   


     
