# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))
            pass

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack or not are_matching(opening_brackets_stack[-1].char, next):
                break
            pass

            opening_brackets_stack.pop();

    return opening_brackets_stack


def main():
    text = input()
    if (text[0] == "I"):
        text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch[-1].position if mismatch else "Success")


if __name__ == "__main__":
    main()
