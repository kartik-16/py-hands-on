import re

REGEX = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$])[a-zA-z0-9@#$]{8,12}$'


def password_validator(string):
    """
    Checks if a password is valid or not based on
    a.Password should contain minimum one capital letter
    b.Password should contain minimum one small letter
    c.Password should contain minimum one special characters from (@#$)
    d.Password should contain minimum one number
    e.Minimum Password length should be of 8 and maximum of 12 characters
    :param string: a string
    :return: Boolean
    """
    return True if re.search(REGEX, string) else False


LIST = ["hello123", "Hello1234", "Hey1234#", "Hey1234#$123455"]

for password in LIST:
    if password_validator(password):
        print(password)
