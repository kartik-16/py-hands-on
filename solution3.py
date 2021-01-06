def manipulate_string(string):
    """
    Returns a reversed string separated by space after making starting of word uppercase
    :param string: a space separated string
    :return: a string
    """

    # we can also use regex for splitting by any white character
    reversed_string = string.split(" ")[::-1]
    return ' '.join([rev.title() for rev in reversed_string])


string = input("Enter the string:\n")
print("String after string formatting:{0}".format(manipulate_string(string)))
