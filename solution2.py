def result_classifier(num):
    """
    Return string based on
    "Failed" if Num < 35
    "Below avg" if 50 > Num >= 35
    "Avg" if 60 > Num >= 50
    "Passed with above avg" if Num >= 60
    :param num: Marks scored
    :return: A String
    """

    if num >= 60:
        return "Passed with above avg"
    elif num >= 50:
        return "Avg"
    elif num >= 35:
        return "Below avg"
    else:
        return "Failed"


try:
    # Expects marks to be integers
    marks = int(input("Enter marks:\n"))
except ValueError as e:
    print("Expected integer:{0}".format(e))
else:
    print(result_classifier(marks))
