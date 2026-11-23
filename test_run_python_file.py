from functions.run_python_file import run_python_file

if __name__ == "__main__":
    # Test 1: main.py (should print the calculator's usage instructions)
    print('Test 1: main.py')
    print(run_python_file("calculator", "main.py"))
    
    # Test 2: main.py with args (should run the calculator)
    print('\nTest 2: main.py with args')
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    
    # Test 3: tests.py (should run the calculator's tests successfully)
    print('\nTest 3: tests.py')
    print(run_python_file("calculator", "tests.py"))
    
    # Test 4: out of bounds error
    print('\nTest 4: ../main.py')
    print(run_python_file("calculator", "../main.py"))
    
    # Test 5: non-existent file error
    print('\nTest 5: nonexistent.py')
    print(run_python_file("calculator", "nonexistent.py"))
    
    # Test 6: not a python file error
    print('\nTest 6: lorem.txt')
    print(run_python_file("calculator", "lorem.txt"))