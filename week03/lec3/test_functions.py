def celsius_to_fahrenheit(celsius):
    """Convert celsius degree to fahrenheit degree"""
    return celsius * 1.8 + 32.0


def is_even(number):
    return number % 2 == 0


def square(number):
    """Square the number."""
    return number ** 2


def main():
    f_degree = celsius_to_fahrenheit(21)
    print(f'{f_degree:.1f}')
    print(is_even(15))
    number = 5
    print(f'{number}^2= {square(number)}')


# start the program
if __name__ == '__main__':
    main()
