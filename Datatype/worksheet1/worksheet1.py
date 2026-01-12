def Q1():
    a=20
    b=10
    print("add :", a+ b)
    print("sub :", a- b)
    print("mul :", a* b)
    print("div :", a/ b)
    print("quotient :", a// b)
    print("product :", a** b)
def Q2():
    a=4.23845
    b=5.23
    print(f"sum a+b ={(a+b):.2f}")
    print(f"sum a+b =",round((a+b),2))
def Q3():
    a="hi"
    b='vishnu'
    print(a+' '+b)
    full_name="%s -> %s"%(a,b)
    print(full_name)
def Q4():
    a=input("Enter str :")
    for n in range(0,5):
        print(a,n)
        print("\n")
    print(a*5)
    print(" ".join([a]*5))
def Q5():
    a=6
    b=10
    print('a==b',a==b)
    print('a!=b',a!=b)
    print('a>b',a>b)
    print('a<b',a<b)
    print('a>=b',a>=b)
    print('a<=b',a<=b)
def Q6():
    a=1
    b=2.10
    c='str'
    d=True
    print(type(a))
    print(type(b))
    print(type(c))
    print(type(d))

def Q7():
    a='50'
    b=int(a)
    c=float(a)
    print(b,c)
def Q8():
    a=25
    b='25'
    print(a+int(b))
def Q9():
    a=1+9j
    b=2+1j
    print(a+b)
    x=complex(3,6)
    y=complex(6,9)
    print(a*b)
    print(x-y)
def Q11():
    l,v,c="Python",3.14,True
    print(l,v,c)
def Q12():
    """Swap two variable values in one line and
    print the values before and after swapping."""
    a=10
    b=50
    print(f'before swap a={a} b{b}')
    a,b=b,a
    print(f'after swap a={a} b{b}')
def Q13():
    '''Assign an integer to a variable, then
     reassign it to a float and string sequentially,
      printing type and value after each step.'''
    a=5
    a=10.10
    a='st'
    print(type(a))
def Q14():
    PI=3.14
    r=3
    print(2*PI*r)
def Q15():
    name="vishnu"
    age=26
    num=10
    print("name : {} age : {} num : {}".format(name,age,num))

def Q16():
    a=5
    b=3
    print(f" a//b = {a//b} a%b = {a%b}")
def Q17():
    a=10
    b=20
    a+=b
    print(a)
def Q18():
    a="python's \"syntax\" is easy "
    print(a)
def Q19():
    a = True
    b = False
    print("True + True =", True + True)
    print("True + False =", True + False)
    print("False + False =", False + False)
    print("True * True =", True * True)
    print("True * False =", True * False)
    print("False * False =", False * False)

def Q21():
    a=2341837493873
    print(a,type(a))
def Q22():
    a=b=c=100
    print(a, b,c)
def Q23():
    a=None
    print(a,type(a))

def Q24():
    a=10
    b=3.5
    r=a+b
    print(r,type(r))
def Q25():
    a="PythonProgramming"
    print(a.split('Programming'))
if __name__=="__main__":
    Q25()
