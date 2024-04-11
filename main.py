def partition(first_numbers: list, second_numbers: list, begin: int, end: int):
    # Right element as pivot
    pivot = first_numbers[end]
    i = begin - 1

    for j in range(begin, end):
        if first_numbers[j] >= pivot:
            i += 1
            (first_numbers[i], first_numbers[j]) = (first_numbers[j], first_numbers[i])
            # Also for the second
            (second_numbers[i], second_numbers[j]) = (second_numbers[j], second_numbers[i])

    (first_numbers[i + 1], first_numbers[end]) = (first_numbers[end], first_numbers[i + 1])
    # Also for the second
    (second_numbers[i + 1], second_numbers[end]) = (second_numbers[end], second_numbers[i + 1])

    return i + 1


def quick_sort_by_first(first_numbers: list, second_numbers: list, begin: int, end: int):
    if begin < end:
        # Pivot  element: left elements - more, right elements - less.
        pivot = partition(first_numbers, second_numbers, begin, end)

        # Left side of pivot
        quick_sort_by_first(first_numbers, second_numbers, begin, pivot - 1)

        # Right side of pivot
        quick_sort_by_first(first_numbers, second_numbers, pivot + 1, end)


def capital_calculation(limit: int, capital: int, gains: list, price: list) -> int:
    # Sort descending
    quick_sort_by_first(gains, price, 0, len(gains) - 1)

    profit = 0
    # Calculation max profit
    for gain, cost in zip(gains, price):
        if limit > 0:
            if capital >= cost and gain > cost:
                capital -= cost
                profit += gain
                limit -= 1
            if not capital:
                break
        else:
            break

    return capital + profit


def input_integer(text: str) -> int:
    while True:
        try:
            number = int(input(f'{text} '))
        except ValueError:
            print('Must be an integer!')
            continue
        if number > 0:
            return number
        else:
            print('Error, at least 1!')


def input_list(text: str) -> list:
    check = False
    while True:
        values = input(f'{text} ')
        new_list = values.split(' ')
        for i, item in enumerate(new_list):
            while True:
                try:
                    new_list[i] = int(new_list[i])
                except ValueError:
                    print('Only numbers separated by spaces!')
                    check = False
                    break
                if new_list[i] >= 0:
                    check = True
                    break
                else:
                    print('Error, there are values less than 0!')
                    check = False
                    break
            if not check:
                break
        else:
            return new_list


def main():
    while True:
        laptop_limit = input_integer('Enter the laptop limit for the summer:')
        capital = input_integer('Enter capital:')
        while True:
            gains = input_list('Enter gains values separated by spaces:')
            price = input_list('Enter price values separated by spaces:')
            if len(gains) != len(price):
                print('The number of profit values must be the same as the number of prices!')
            else:
                break

        result = capital_calculation(laptop_limit, capital, gains, price)
        print(f'Capital at the end of summer: {result}')

        control = input('Continue? (y/n): ')
        if control == 'n':
            break


if __name__ == '__main__':
    main()

