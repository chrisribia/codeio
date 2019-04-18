import re  # import the regexp module


def get_password(text):
    return input(text)


def validate_password():
    """ Define a function to validate password """
    while True:
        password = get_password("Input your password: ")

        if (len(password) < 6 or len(password) > 12):
            return(
                "INVALID: Password should have minumum of 6 characters and maximum of 12 characters")
        elif re.search('[a-z]', password) is None:
            return("INVALID: Password should contain at least a lowercase character")
        elif re.search('[0-9]', password) is None:
            return("INVALID: Password should contain at least a number")
        elif re.search('[A-Z]', password) is None:
            return("INVALID: Password should contain at least a capital character")
        elif re.search('[$#@]', password) is None:
            return("INVALID: Password should contain at least a special character")
        else:
            return("Your password is VALID")
            break

#print(validate_password())
