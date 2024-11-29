class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        area=self.length*self.breadth
        return area
    def peri(self):
        peri=2*(self.length+self.breadth)
        return peri
length=int(input("Enter the Length of Rectangle"))
breadth=int(input("Enter the Breadth of Rectangle"))
r1=rectangle(length,breadth)
while 1:
    choice=int(input("Enter the choice..1.Area,2.Perimeter,3.Exit"))
    if choice==1:
        print("The area of rectangle is",r1.area())
    elif choice==2:
        print("The perimeter of rectangle is",r1.peri())
    else:
        exit()