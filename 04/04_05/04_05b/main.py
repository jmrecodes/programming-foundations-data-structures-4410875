def has_unique_characters(data):
    # set_of_letters = set([]);

    # for letter in data:
    #     if (letter not in set_of_letters):
    #         set_of_letters.add(letter)
    #     else:
    #         return False
    
    # return True

    unique_data = set(data)

    return len(unique_data) == len(data)

print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
