from functions.get_file_content import get_file_content

if __name__ == "__main__":
    # Test 1: lorem.txt (Truncation check)
    print("Test 1: lorem.txt")
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")
    
    # Test 2: main.py
    print("\nTest 2: main.py")
    print(get_file_content("calculator", "main.py"))
    
    # Test 3: pkg/calculator.py
    print("\nTest 3: pkg/calculator.py")
    print(get_file_content("calculator", "pkg/calculator.py"))
    
    # Test 4: /bin/cat (Out of bounds)
    print("\nTest 4: /bin/cat")
    print(get_file_content("calculator", "/bin/cat"))
    
    # Test 5: pkg/does_not_exist.py (File not found)
    print("\nTest 5: pkg/does_not_exist.py")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))