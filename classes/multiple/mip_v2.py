class Base1(object):
    def __init__(self):
        print("Base1 initializing.")

    def __del__(self):
        print("Base1 destroying.")

class Base2(object):
    def __init__(self, name):
        print("Base2 initializing.")

    def __del__(self):
        print("Base2 destroying.")

class Derived(Base1, Base2):
    def __init__(self):
        # Note - in Python2 this would be super(Derived, self).__init__()
        super().__init__()
        print("Derived initializing.")

    def __del__(self):
        print("Derived destroying.")
        super().__del__()

test = Derived()
print(Derived.mro())
del test
