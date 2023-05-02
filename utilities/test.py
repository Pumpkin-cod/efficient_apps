
def get_gst_check(number):
    """
    This function returns the last digit of the GST number.
    The output is the last digit which should match the given 14-digit number.
    :param number: This is the only argument that needs to be given. It is a mandatory argument.
                   The argument must be at least 14 digits long.
    :type number: str
    :return: The function will return the correct last digit of the given GST number.
    :raises TypeError: If the parameter entered is not a string.
    :raises ValueError: If the parameter entered is not at least 14 digits long.
    :seealso: To know how the GST Checksum is calculated, see the algorithm behind the last digit.
    """
    if not isinstance(number, str):
        raise TypeError("Only strings are allowed")

    if len(number) < 14:
        raise ValueError("Please ensure that the input is at least 14 digits long")

    char_list = [char.upper() for char in number]
    multipliers = [2 if i % 2 == 1 else 1 for i in range(14)]

    cum_hash = []
    for i, char in enumerate(char_list[:14]):
        if char.isdigit():
            value = int(char)
        else:
            value = ord(char) - 55

        prod = value * multipliers[i]
        quotient = prod // 36
        remainder = prod % 36
        hash_val = quotient + remainder

        cum_hash.append(hash_val)

    hash_sum = sum(cum_hash)
    remainder = hash_sum % 36
    checksum = 36 - remainder

    if checksum < 10:
        final_check = str(checksum)
    elif checksum == 36:
        final_check = "0"
    else:
        final_check = chr(checksum + 55)

    return final_check



last=get_gst_check("10AAACI1681G1Z")

print(last)