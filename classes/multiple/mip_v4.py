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
        Base1.__init__(self)
        Base2.__init__(self, "Works!")
        print("Derived initializing.")

    def __del__(self):
        print("Derived destroying.")
        Base2.__del__(self)
        Base1.__del__(self)

test = Derived()
del test
