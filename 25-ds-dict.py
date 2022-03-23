# Dictionary
# Key- Value Pairs
# Name -> contact

point={"x":1,"y":2}
print(point)

point=dict(x=1,y=2)
print(point)

point["x"]=10
point["y"]=20
point["z"]=30
print(point)

#----------------------
print("A",point.get("a",0))

if "a" in point:
    print(point["a"])

print("X",point.get("x"))



for key in point:
    print(key,point[key])

for key,value in point.items():
    print(key,value)