#  Test Credit Card Number: 4532689602924663 (VALID)
#  Test Credit Card Number: 4270557025643724 (INVALID)

import re

def sum_digits(digit):
    if digit < 10:
        return digit
    else:
        sum = (digit % 10) + (digit // 10)
        return sum

def format_card(ccn):
    return re.sub(r"\D", "", ccn)

ccn = input("Enter a credit card number: ")
checked_ccn = format_card(ccn)
numbers = list(checked_ccn)

a = checked_ccn
b = str(a)
list = []

for digit in b:
    list.append (int(digit))

check_digit = list[-1]
list = list[:-1]

l = list[:]
l[::2] = [x*2 for x in l[::2]]

l = [sum_digits(x) for x in l]
l = sum(l)
l = l + check_digit

valid_or_invalid = l % 10 == 0

if valid_or_invalid == True:
    print("This card number is valid")
else:
    print("This card number is invalid")
