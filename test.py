class A:
    def __init__(self):
        print("A's init called")

class B(A):
    def __init__(self):
        super().__init__()
        print("B's init called")

class C(A):
    def __init__(self):
        super().__init__()
        print("C's init called")

class D(B, C):
    def __init__(self):
        super().__init__()
        print("D's init called")

d = D()
