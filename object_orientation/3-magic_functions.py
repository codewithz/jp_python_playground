class Point:
    color='Red'
    def __init__(self,x,y):
        print('Point Constructor')
        self.x=x;
        self.y=y;


    def draw(self):
        print(f"Point({self.x},{self.y})")

    def __str__(self):
        return f"Point({self.x},{self.y})"




p1=Point(1,2)
print(p1)

print(isinstance(p1,object))

o=object();
