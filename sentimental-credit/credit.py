# TODO
from cs50 import get_string
import re


def check(num):
    # digits conseuctive to second to last digit
    sum1 = 0
    # sum of the rest of digits
    sum2 = 0
    n = 1
    for digit in num[::-1]:
        if n % 2 == 0:
            new_digit = int(digit) * 2
            if new_digit > 9:
                for subdigit in str(new_digit):
                    sum1 += int(subdigit)
            else:
                sum1 += new_digit

        else:
            sum2 += int(digit)
        n += 1

    if (sum1 + sum2) % 10 == 0:
        return True

    return False


def main():

    num = get_string("Number: ")

    if len(num) != 13 and len(num) != 15 and len(num) != 16:
        print("INVALID\n")

    elif re.match(r'^(34|37)\d{13}$', num):
        if check(num):
            print("AMEX\n")
        else:
            print("INVALID\n")

    elif re.match(r'^(51|52|53|54|55)\d{14}$', num):
        if check(num):
            print("MASTERCARD\n")
        else:
            print("INVALID\n")

    elif re.match(r'^4\d{12}(?:\d{3})?$', num):
        if check(num):
            print("VISA\n")
        else:
            print("INVALID\n")
    else:
        print("INVALID\n")


main()