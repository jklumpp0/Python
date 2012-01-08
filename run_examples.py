def test_multi_inheritance():
    from classes.multiple import run_example
    run_example()

def print_test(msg, func):
    print()
    print(msg)
    print("=" * len(msg))
    func()
    print()

if __name__ == '__main__':
    print("Running all examples.")
    
    # Multiple inheritance
    print_test("Multiple Inheritance Example", test_multi_inheritance)

