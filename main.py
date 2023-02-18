# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if not opening_brackets_stack:
                return i+1

            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next):
                return i+1

    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return "Success"


def main():
    input_type = input("Enter F to read from file or I to input the brackets manually: ")
    if input_type.lower() == "f":
        
        filename = input("Enter file name: ")
        with open(filename) as f:
            text = f.read()
    elif input_type.lower() == "i":
        text = input("Enter brackets: ")
    else:
        print("Invalid input type")
        return

    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()
