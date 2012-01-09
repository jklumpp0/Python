class Base1(object):
    def __init__(self):
        super().__init__()
        print("Base1 initializing.")

    def __del__(self):
        print("Base1 destroying.")
        super().__del__()

class Base2(object):
    def __init__(self, name):
        super().__init__()
        print("Base2 initializing.")

    def __del__(self):
        print("Base2 destroying.")
        super().__del__()

class DerivedFails(Base1, Base2):
    def __init__(self):
        # Note - in Python2 this would be super(Derived, self).__init__()
        super().__init__()
        print("Derived initializing.")

    def __del__(self):
        print("Derived destroying.")
        super().__del__()

class DerivedWorks(Base2, Base1):
    def __init__(self):
        # Note - in Python2 this would be super(Derived, self).__init__()
        super().__init__("Works!")
        print("Derived initializing.")

    def __del__(self):
        print("Derived destroying.")
        super().__del__()

try:
    test = DerivedFails()
except TypeError as te:
    print(te)

test = DerivedWorks()
del test
