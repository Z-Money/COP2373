import re

def validateValue(pattern, value):
    """
    Validate a phone based on its format

    Parameters:
        pattern (regex): Regex to check against the passed value variable
        value (str): Value to check

    Variables:
        isValid (bool): True or False based on value's validity

    Logic:
        1. Check the provided value against the regex and convert to a boolean
        2. Return the boolean value

    Returns:
        isValid (bool): True if value matches pattern, False otherwise
    """
    isValid = bool(re.match(pattern, value))
    return isValid

def printIfValid(label, is_valid):
    """
    Evaluates if the provided value is valid or not

    Parameters:
        label (str): Label to check
        is_valid (bool): True or False based on value's validity

    Variables:
        None

    Logic:
        1. Prints if the label is valid or not based on whether its True/False

    Returns:
        None
    """
    print(f"{label} is {"valid" if is_valid else "not valid"}")

def main():
    """
    Prompts user from their personal information, then validates it

    Parameters:
         None

    Variables:
        PHONE_NUMBER_REGEX (str): Regular expression to validate the phone number
        SSN_REGEX (str): Regular expression to validate the SSN
        ZIP_CODE_REGEX (str): Regular expression to validate the zip code
        phoneNumber (str): User-inputted phone number
        ssn (str): User-inputted social security number
        zipCode (str): User-inputted zip code

    Logic:
        1. Prompt user for phone number, ssn, and zip code
        2. Print the validity of the user's phone number, ssn, and zip code
    """
    PHONE_NUMBER_REGEX = re.compile(r"^\d{3}-\d{3}-\d{4}$")
    SSN_REGEX = re.compile(r"^\d{3}-\d{2}-\d{4}$")
    ZIP_CODE_REGEX = re.compile(r"^\d{5}$")


    phoneNumber = input("Enter a phone number: ")
    ssn = input("Enter a SSN: ")
    zipCode = input("Enter a zip code: ")

    print("\n---Verification---")
    printIfValid("Phone Number", validateValue(PHONE_NUMBER_REGEX, phoneNumber))
    printIfValid("SSN", validateValue(SSN_REGEX, ssn))
    printIfValid("Zip Code", validateValue(ZIP_CODE_REGEX, zipCode))


if __name__ == "__main__":
    main()