class Math:
    #static method cannot have self parameter
    def add(a,b):
        return a+b;

    @staticmethod
    def mul(a,b):
        return a*b;

# Two ways to make a function static
# 1. Use the inbuilt staticmethod function
# 2. Use a decorator @staticmethod on top of the function

Math.add=staticmethod(Math.add)
print("Add-->",Math.add(1,2))
print("Mul-->",Math.mul(3,2))