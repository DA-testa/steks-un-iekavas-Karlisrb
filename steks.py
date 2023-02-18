def check_brackets(s):
    stack = []
    opening_brackets = "([{"
    closing_brackets = ")]}"
    matching_brackets = {"(": ")", "[": "]", "{": "}"}

    for i, char in enumerate(s):
        if char in opening_brackets:
            stack.append((char, i))


        elif char in closing_brackets:
            if not stack:
                return i + 1
            open_bracket, open_index = stack.pop()

            
            if matching_brackets[open_bracket] != char:
                return i + 1

    if stack:
        open_bracket, open_index = stack.pop()
        return open_index + 1

    return "Success"

if input("Use an input to choose files or input - F or I: ") == "F":
    file_path = input("Enter file path: ")
    brackets = ""
    try:
        with open(file_path) as file:
            brackets = file.readline().strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit()
else:
    brackets = input("Enter brackets: ")
    file_path = input("Enter file path to save brackets (leave empty to skip): ")

result = check_brackets(brackets)

if result == "Success":
    print(result)
else:
    if result <= len(brackets):
        print(f"{result}")
    else:
        print(f"{result - len(brackets)}")

if file_path:
    try:
        with open(file_path, 'w') as file:
            file.write(brackets)
            print(f"Brackets saved to file '{file_path}'.")
    except IOError:
        print(f"Error: Cannot write to file '{file_path}'.")