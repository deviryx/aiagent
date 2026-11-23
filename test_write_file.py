from functions.write_file import write_file

if __name__ == "__main__":
    # Test 1: Overwriting an existing file
    print('Test 1: lorem.txt')
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
    
    # Test 2: Writing a new file in a subdirectory
    print('\nTest 2: pkg/morelorem.txt')
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
    
    # Test 3: Attempting to write outside the working directory
    print('\nTest 3: /tmp/temp.txt')
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))