# function will convert string parameter to upper case
def to_upper(text):
    if type(text) != str:
        raise TypeError('Parameter should be str') 
    return text.upper()


# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    for word in str_list:
        if word.islower():
            return False
    return True

"""# function will convert string parameter to upper case
def to_upper(text):
    if not isinstance(text, str):
        raise TypeError('Parameter should be str')
    return text.upper()

# function will check return true if all items on
# the parameter list are upper case
def to_word_list_isupper(str_list):
    if not isinstance(str_list, list):
        raise TypeError('Parameter should be list')
    for word in str_list:
        if not isinstance(word, str):
            raise TypeError('All items in the list should be str')
        if not word.isupper():
            return False
    return True"""
