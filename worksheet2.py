def Q1():
    a=b=10
    b=20
    print(a)
def Q2():
    x = 2
    y = 2.0
    z = "2"
    w = x + int(z)
    v = str(x) + z
    print(w,v)
def Q4():
    x=[1,2,3]
    y=x
    x[0]=9
    print(x,y)
def Q5():
    a=3
    b=3.0
    if a==b:
        print(True)
    else:
        print(False)
def Q6():
    a=(5)
    b=(5,)
    print(type(a))
    print(type(b))
def Q9():
    a = 3   
    b = 3.5  
    result_add = a + b
    print("3 + 3.5 =", result_add, "| type:", type(result_add))
    result_mul = a * b
    print("3 * 3.5 =", result_mul, "| type:", type(result_mul))
    result_div = a / 2
    print("3 / 2 =", result_div, "| type:", type(result_div))
def Q10():
        a = "5"
        b = 5
        c = a * b
        d = b * a
        print(c, d)
def Q14():
    x = [1, 2, 3]
    y = x
    x = [4, 5, 6]
    print(y)
if __name__=="__main__":
    Q14()
    
