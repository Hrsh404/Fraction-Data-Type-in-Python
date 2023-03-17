class Fraction:
    def __init__(self,n,d):
        self.__num=n
        self.__den=d

#For Fraction Addition
    def __add__(self, other):
        temp_num=self.__num *other.__den +other.__num *self.__den
        temp___den=self.__den*other.__den
        return f"{temp_num}/{ temp___den}"

#For Fraction Substraction
    def __sub__(self, other):
        temp_num=self.__num *other.__den -  other.__num *self.__den
        temp___den=self.__den*other.__den
        return f"{temp_num}/{ temp___den}"

#For Fraction Multiplicaton
    def __mul__(self, other):
        temp_num=self.__num * other.__num 
        temp___den=self.__den*other.__den
        return f"{temp_num}/{ temp___den}"

#For Fraction Divison
    def __truediv__(self, other):
        temp_num=self.__num *other.__den 
        temp___den=self.__den*other.__den
        return f"{temp_num}/{ temp___den}"
    
   
    def __str__(self):
        return f"{self.__num}/{self.__den}  "
#For Simplification of Fraction
    def simplify(self):
       
        
        print(self.__num/self.__den)


    

    


f1=Fraction(3,4)
f2=Fraction(5,6) 
f3=Fraction(9,6)

#Try These codes

print(f1)
print(f2)
print(f1+f2)
print(f1/f2)
f1.simplify()



