import string
import sys


def ft_count_char(text: str) -> None:

    uppers = 0
    lowers = 0
    digits = 0
    spaces = 0
    punctuations = 0

    lenth = len(text)
    for char in text:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        elif char in string.punctuation:
            punctuations += 1

    print(f"The text contains {lenth} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 1 or sys.argv[1] is None:
            try:
                print("What is the text to count?")
                text = sys.stdin.read()
            except KeyboardInterrupt:
                return
        else:
            text = sys.argv[1]

        ft_count_char(text)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
