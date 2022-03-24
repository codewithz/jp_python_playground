import  constant;


class Point:
    color='Red'
    def __init__(self,x,y):
        print('Point Constructor')
        self.x=x;
        self.y=y;
        print(constant.PI)

    def draw(self):
        print(f"Point({self.x},{self.y})")


print(Point.color)

p=Point(1,2)
p.draw()
print(p.color)

Point.color='Green'

p1=Point(3,4)
p1.draw()
print(p1.color)

