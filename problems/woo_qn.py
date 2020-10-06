# Given a number N and a pattern, evaluate it 
# A number can be as many digits, maximum 12 digits, no leading zeroes
# Then a pattern afterwards
# for example ab+cd
# 55555 a+bcde
# Can either be a plus or minus
# Maximum either one plus or minus sign
# '1234 ab+cd' string input should give 46

# Handle edge case 
# or something like 102 a+bc 

import typing
import re

class DataWrapper:
    number_lookup : dict = {}
    first_number : str = ''
    token = ''
    second_number: str = ''

stringlookup = 'abcdefghijkl'

def parse_string(input_str: str) -> DataWrapper:
    data = DataWrapper()
    first_token, rest_of_string = re.split(" ", input_str)
    # Parse second part of string
    for (index, number) in enumerate(first_token):
        data.number_lookup[stringlookup[index]] = number
    
    # Get token 
    if '+' in rest_of_string:
        data.first_number, data.second_number = rest_of_string.split("+")
        data.token = '+'
    elif '-' in rest_of_string:
        data.first_number, data.second_number = rest_of_string.split("-")
        data.token = '-'
    
    return data

def replace_letters_with_numbers(letter_string: str, number_lookup) -> int:
    # 'ab' -> 12
    number_string = ''
    for letter in letter_string:
        number_string += number_lookup[letter]

    return int(number_string)

def solution(input_str: str) -> int :
    parsed_data = parse_string(input_str)

    first_number = replace_letters_with_numbers(parsed_data.first_number, 
    parsed_data.number_lookup)
    second_number = replace_letters_with_numbers(parsed_data.second_number, 
    parsed_data.number_lookup)

    if parsed_data.token == '+':
        return first_number + second_number
    elif parsed_data.token == '-':
        return first_number - second_number
    else:
        raise ValueError

if __name__ == "__main__":
    print(solution("1520 ab+cd"))
    print(solution("1502 ab+cd"))
    print(solution("1520 ab-cd"))
    print(solution("199999999999 a-bcdefghijkl"))