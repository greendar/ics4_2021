class A:
    def __init__(self):
        print('class A: Constructed')

    def __del__(self):
        print('class A: Destructed')

class B:
    def __init__(self):
        print('class B: Constructed')

    def __del__(self):
        print('class B: Destructed')

class C(A):
    def __init__(self):
        print('class C: Constructed')


    def __del__(self):
        print('class C: Destructed')


a = A()
b = B()
c = C()
