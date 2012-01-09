class Base1(object):
    def __init__(self):
        print("Base1 initializing.")

    def __del__(self):
        print("Base1 destroying.")

class Base2(object):
    def __init__(self):
        print("Base2 initializing.")

    def __del__(self):
        print("Base2 destroying.")

class Derived(Base1, Base2):
    def __init__(self):
        print("Derived initializing.")

    def __del__(self):
        print("Derived destroying.")

test = Derived()
del test
