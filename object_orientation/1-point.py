#Function Variales -- Snake Casing -- one_two_three_four
#Class -------------- Pascal Casing -- OneTwoThreeFour


class Point:
    def draw(self):
        print('Draw')

p=Point();
p.draw()
print(type(p))

print(isinstance(p,Point))
print(isinstance(p,int))
