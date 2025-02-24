def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ...
            for line in f:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '" + filename + "' not found.")

function_with_closed_file("my_file.txt")
