class D: pass
class E: pass
class B(D, E): pass
class C: pass
class A(B, C): pass

x = A()
print(isinstance(x, A)) # True
print(isinstance(x, B)) # True
print(isinstance(x, object)) # True
print(isinstance(x, str)) # False