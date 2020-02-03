def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def mod(a,b):
    return a%b

def div(a,b):
    return a/b


# +
# Vector Arithmetics
# Import System Mudule

# +
# Fuction for Vector Addition

def addVec(x,y):
    return [x[i] + y[i] for i in range(len(x))]


# +
# Fuction for Vector Subtraction

def subVec(x,y):
    return [x[i] - y[i] for i in range(len(x))]


# +
# Fuction for Vector Scalar Multiplication

def mulVec(x,p):
    return [p*x[i] for i in range(len(x))]


# +
# Fuction for Vector Dot Product

def dotVec(x,y):
    return [x[i] * y[i] for i in range(len(x))]
# -


