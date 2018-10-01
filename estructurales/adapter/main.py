from adapters import NumbersList


def main():
    numbers_list = NumbersList()

    print("get first 10 even numbers")

    print(numbers_list.ten_first_evens())

    print("get first 10 odd numbers")

    print(numbers_list.ten_first_odds())


if __name__ == '__main__':
    main()
