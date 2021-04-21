"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    even_nums = []
    for num in nums:
        if num%2 == 0:
            even_nums.append(num)
    return even_nums


def get_odd_indices(items):
    result = []

    for idx in range(len(items)):
        if idx % 2 != 0:
            result.append(items[idx])
        
    return result


def print_as_numbered_list(items):
    i = 1
    for item in items:
        print(f'{i}. {item}')
        i += 1


def get_range(start, stop):
    nums = []
    num = start

    while num < stop:
        nums.append(num)
        num += 1
    


def censor_vowels(word):
    chars = []

    for letter in word:
        if letter in ['a','e','i','o','u']:
            chars.append("*")
        else:
            chars.append(letter)
    
    return ''.join(chars)


def snake_to_camel(string):
    camel_case = []
    input_string = string.split("_")

    for word in input_string:
        camel_case.append(f'{word[0].upper()}{word[1:]}')
    
    return ''.join(camel_case)


def longest_word_length(words):
    longest = len(words[0])

    for word in words:
        if len(word) > longest:
            longest = word

    return longest


def truncate(string):
    result = []

    for char in string:
        if len(result)==0 or char!= result[len(result)-1]:
            result.append(char)
    return ''.join(result)


def has_balanced_parens(string):
    parens = 0

    for char in string:
        if char=='(':
            parens += 1
        if char ==')':
            parens -= 1
    
    if parens<0:
        return False
    
    return True


def compress(string):
    pass  # TODO: replace this line with your code
