from classes.lifecycle import LifeCyclePrinter

class Multiple(object):
    """
    Test multiple inheritance
    - duh
    """
    def __init__(self):
        super().__init__()
        print("Multiple was called!")


class DemoClass(LifeCyclePrinter, Multiple):
    """
    A demo class
    """

    def __init__(self, name):
        """
        Initialize!
        """
        super(DemoClass, self).__init__(name)
        self.read_bytes = 0

    def close(self):
        """
        Close the stream!
        - That's how it goes!
        """
        print("{} is closing...".format(self.name))

    def read(self, size):
        to_read = self.read_bytes + len(self.name)

        if to_read > len(self.name):
            to_read = len(self.name)

        to_return = self.name[self.read_bytes:to_read]
        self.read_bytes = to_read
        return to_return

    def __iter__(self):
        class Iteratorz(LifeCyclePrinter):
            def __init__(inner_self, name="Default Iteratorz"):
                super(Iteratorz, inner_self).__init__(name)
                inner_self.read = 0

            def __iter__(inner_self):
                return inner_self

            def __next__(inner_self):
                next_stop = inner_self.read + 2
                if next_stop > len(self.name):
                    next_stop = len(self.name)

                if next_stop == inner_self.read:
                    raise StopIteration()

                next_str = self.name[inner_self.read:next_stop]
                inner_self.read = next_stop
                return next_str

        print("{} is creating an iterator.".format(self.name))
        return Iteratorz()

# Main program
if __name__ == "__main__":
    print("App initializing...")
    x = DemoClass("Simple")

    print("Trying with statement...")
    with DemoClass("With an iterator!") as w:
        for line in w:
            print(line)
