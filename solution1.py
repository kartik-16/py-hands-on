def concatenate_strings(str1, str2):
    """
    Returns concatenated strings of input two strings
    :param str1: First input String
    :param str2: Second input String
    :return: A concatenated string
    """
    return "{0}{1}".format(str1, str2)


var1 = input("Enter first string:\n")
var2 = input("Enter second number:\n")
print(concatenate_strings(var1, var2))

