#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

# From Kevin
CONVERT_STRING = string.digits + string.ascii_lowercase
BASE_DECODE = {digit: val for val, digit in enumerate(CONVERT_STRING)}


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    
    # personal decode
    # digits = digits[::-1]
    # decoded = 0

    # for exponent, digit in enumerate(digits):
    #     power = power(base,exponent)

    #     if digit.isalpha():
    #         digit = digit.lower()
    #         digit = ord(digit) - 97 + 10
    #     else:
    #         digit = int(digit)
        
    #     decoded += digit * power
    
    # return decoded

    # Kevin's Decode.
    decoded = 0

    for i, digit in enumerate(reversed(digits)):
        decoded += (pow(base, i) * BASE_DECODE[digit])
    return decoded


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    # personal encode
    # encoded_val = ""
    
    # while number > 0:
    #     number, remainder = divmod(number, base)
        
    #     if remainder >= 10:
    #         encoded_val += chr(remainder + 87)
    #     else:
    #         encoded_val += str(remainder)

    # return encoded_val[::-1]

    # Using Kevin's function
    if number < base:
        return CONVERT_STRING[number]

    div, mod = divmod(number, base)

    return encode(div, base) + CONVERT_STRING[mod]


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    
    return encode(decode(digits, base1), base2)


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')

if __name__ == '__main__':
    main()