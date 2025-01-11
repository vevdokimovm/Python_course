class A:
    pass

class B(A):
    pass

class C:
    pass

class D(C):
    pass

class E(B, C, D):
    pass

print(E.mro()) # TypeError: Cannot create a consistent method resolution
               # order (MRO) for bases object, C, D