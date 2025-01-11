class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

x = A()
print(issubclass(A, A)) # True
print(issubclass(C, D)) # False
print(issubclass(A, D)) # True
print(issubclass(C, object)) # True
print(issubclass(object, C)) # False