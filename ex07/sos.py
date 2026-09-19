import sys


NESTED_MORSE = {
    " ": "/ ",
    "A": ".- ",
    "B": "-... ",
    "C": "-.-. ",
    "D": "-.. ",
    "E": ". ",
    "F": "..-. ",
    "G": "--. ",
    "H": ".... ",
    "I": ".. ",
    "J": ".--- ",
    "K": "-.- ",
    "L": ".-.. ",
    "M": "-- ",
    "N": "-. ",
    "O": "--- ",
    "P": ".--. ",
    "Q": "--.- ",
    "R": ".-. ",
    "S": "... ",
    "T": "- ",
    "U": "..- ",
    "V": "...- ",
    "W": ".-- ",
    "X": "-..- ",
    "Y": "-.-- ",
    "Z": "--.. ",
    "0": "----- ",
    "1": ".---- ",
    "2": "..--- ",
    "3": "...-- ",
    "4": "....- ",
    "5": "..... ",
    "6": "-.... ",
    "7": "--... ",
    "8": "---.. ",
    "9": "----. ",
}


def encode_morse(text: str) -> str:
    morse_list = []
    for char in text.upper():
        if char not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        morse_list.append(NESTED_MORSE[char])

    return "".join(morse_list).rstrip()


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        arg = sys.argv[1]

        if not isinstance(arg, str):
            raise AssertionError("the arguments are bad")

        result = encode_morse(arg)
        print(result)

    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
