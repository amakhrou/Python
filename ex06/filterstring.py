import sys
from ft_filter import ft_filter


def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]

        try:
            min_len = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")

        words = text.split()
        result = list(ft_filter(lambda w: len(w) > min_len, words))

        print(result)
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    main()
