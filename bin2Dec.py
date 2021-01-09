#!/usr/bin/env python3
# bin2Dec.py - turn decimals into binary and vice versa

def bin_2_Dec(num):
    decimal = 0
    for digit in num:
        decimal = decimal * 2 + int(digit)
    print(decimal)

def base10_as_base(num, base):
    output = ''
    while num > 0:
        output = str(num % base) + output
        num //= base
    print(output)
    return output


if __name__ == '__main__':
    try:
        b = input('Please enter either a binary or regular integer. \n')
        check = 0
        for i in range(len(b)):
            if b[i] not in ['0', '1']:
                base10_as_base(int(b), 2)
                check += 1
                break
        while check == 0:
            a = str(input('Did you input a binary number? type y/n \n'))
            if a == 'y':
                bin_2_Dec(b)
                break
            if a == 'n':
                base10_as_base(int(b), 2)
                break
            if a != 'y' or a != 'n':
                print('Please answer y/n.')
                continue
    except (ValueError, SyntaxError):
        print('That was not a number.')

