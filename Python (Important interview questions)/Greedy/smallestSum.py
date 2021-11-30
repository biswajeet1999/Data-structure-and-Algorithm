def findSmallest(m,s):
    if (s == 0):       
        if(m == 1):
              print("Smallest number is 0")
        else :
              print("Not possible")
        return
    if (s > 9*m):  
        print("Not possible")
        return
  
    res=[0 for i in range(m+1)]
    s -= 1
    for i in range(m-1,0,-1):
        if (s > 9):
            res[i] = 9
            s -= 9
        else:
            res[i] = s
            s = 0
    res[0] = s + 1                
    print("Smallest number is ",end="")
    for i in range(m):
        print(res[i],end="")
 
 
s = 9
m = 6
findSmallest(m, s)
 




# class Complex:
#    def __init__(self, real, ima=0):
#       self.real = real
#       self.ima = ima
#    def add(self, c1):
#       newReal = self.real + c1.real
#       newIma = self.ima + c1.ima
#       return Complex(newReal, newIma)

# c1 = Complex(1, 2)
# c2 = Complex(2, 3)
# print(c1.real, c1.ima)


# public Complex {
#    private int real, ima;

#    // constuctor with 2 argument
#    public Complex(int real, imt ima) {
#       this.real = real;
#       this.ima = ima;
#    }
#    // construcot with 1 argument
#    public Complex(int real) {
#       this.real = real;
#    }
#    // ocnstructor with no argument
#    public Complex() { }

#    // setters
#    public void setReal(int real) {
#       this.real = real;
#    }
#    public void setIma(int ima) {
#       this.ima = ima;
#    }

#    // getters
#    public int getReal() {
#       return this.real;
#    }
#    public int getIma() {
#       return this.ima;
#    }

#    public void add(Complex obj) {
#       this.real = this.real + obj.real;
#       this.ima = this.ima + obj.ima;
#    }

# }