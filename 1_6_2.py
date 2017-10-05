class D: pass
class E: pass
class B(D,E): pass
class C: pass
class A(B,C): pass

issubclass(A,A)
issubclass(C,D)
issubclass(A,D)
issubclass(C,object)
issubclass(object,C)

x = A()
isinstance(x,A)
isinstance(x,B)
isinstance(x,object)
isinstance(x,str)

# MRO stands for Method Resolution Order
print(A.mro())