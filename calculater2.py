#CACLULATER

#importing the function math to do the sums
import math
#writing the code by defining functions and storing the output
def sq(n):
    return (n*n)

def sqrt(n):
    return math.sqrt(n)

def cb(n):
    return(n**3)

def fact(n):
    return math.factorial(n)

#def power(x,y):
    #return (x**y)

#def root(x,y):
    #return (x**1/y)

def log(n):
    return math.log(n)

def sin(n):
    return math.sin(n)

def tan(n):
    return math.tan(n)

def cos(n):
    return math.cos(n)

def sinh(n):
    return math.sinh(n)

def cosh(n):
    return math.cosh(n)

def tanh(n):
    return math.tanh(n)

def mod(n):
    return math.mod(n)

def ceil(n):
    return math.ceil(n)

def fabs(n):
    return math.fabs(n)

def floor(n):
    return math.floor(n)

def frexp(n):
    return math.frexp(n)

def isfinite(n):
    return math.isfinite(n)

def isinf(n):
    return math.isinf(n)

def isqrt(n):
    return math.isqrt(n)

def isnan(n):
    return math.isnan(n)

def modf(n):
    return math.modf(n)

def trunc(n):
    return math.trunc(n)

def ulp(n):
    return math.ulp(n)

def exp(n):
    return math.exp(n)

def expm1(n):
    return math.expm1(n)

def log1p(n):
    return math.log1p(n)

def log2(n):
    return math.log2(n)

def log10(n):
    return math.log10(n)

def acos(n):
    return math.acos(n)

def asin(n):
    return math.asin(n)

def atan(n):
    return math.atan(n)

def degrees(n):
    return math.degrees(n)

def radians(n):
    return math.radians(n)

def acosh(n):
    return math.acosh(n)

def asinh(n):
    return math.asinh(n)

def atanh(n):
    return math.atanh(n)

def add(n):
    x=float(input("Put other number here:  "))
    return (n+x)

def subtract(n):
    x=float(input("Put number being subtracted here:  "))
    return (n-x)

def multiply(n):
    x=float(input("Put other number here:  "))
    return (n*x)

def divide(n):
    x=float(input("Put dividend here:  "))
    return (n/x)

#doing commands when user uses this calc
def calc(imput,n):
    if imput == 'sq':
        return sq(n)
    if imput == 'sqrt':
        return sqrt(n)
    if imput == 'cb':
        return cb(n)
    if imput == 'fact':
        return fact(n)
    if imput == 'log':
        return log(n)
    if imput == 'sin':
        return sin(n)
    if imput == 'tan':
        return tan(n)
    if imput == 'cos':
        return cos(n)
    if imput == 'sinh':
        return sinh(n)
    if imput == 'cosh':
        return cosh(n)
    if imput == 'tanh':
        return tanh(n)
    if imput == 'mod':
        return mod(n)
    if imput == 'ceil':
        return ceil(n)
    if imput == 'fabs':
        return fabs(n)
    if imput == 'floor':
        return floor(n)
    if imput == 'frexp':
        return frexp(n)
    if imput == 'isfinite':
        return isfinite(n)
    if imput == 'isinf':
        return isinf(n)
    if imput == 'isqrt':
        return isqrt(n)
    if imput == 'isnan':
        return isnan(n)
    if imput == 'modf':
        return mof(n)
    if imput == 'trunc':
        return trunc(n)
    if imput == 'ulp':
        return ulp(n)
    if imput == 'exp':
        return exp(n)
    if imput == 'expm1':
        return expm1(n)
    if imput == 'log1p':
        return log1p(n)
    if imput == 'log2':
        return log2(n)
    if imput == 'log10':
        return log10(n)
    if imput == 'acos':
        return acos(n)
    if imput == 'asin':
        return asin(n)
    if imput == 'atan':
        return atan(n)
    if imput == 'degrees':
        return degrees(n)
    if imput == 'radians':
        return radians(n)
    if imput == 'acosh':
        return acosh(n)
    if imput == 'asinh':
        return asinh(n)
    if imput == 'atanh':
        return atanh(n)
    if imput == 'add':
        return add(n)
    if imput == 'subtract':
        return subtract(n)
    if imput == 'multiply':
        return multiply(n)
    if imput == 'divide':
        return divide(n)
