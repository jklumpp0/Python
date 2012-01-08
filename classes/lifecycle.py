class LifeCyclePrinter(object):
    """
    Print lifecycle events
    """

    def __init__(self, name):
        super().__init__()
        self.name = name
        print("{} is initializing...".format(self.name))

    def __del__(self):
        print("{} is destroying.".format(self.name))

    def __enter__(self):
        print("{} is entering a with statement.".format(self.name))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("{} is exiting a with statement.".format(self.name))

