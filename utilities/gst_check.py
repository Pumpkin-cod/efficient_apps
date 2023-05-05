import re
import pandas as pd

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
        print(type(number))
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



def gstchecksum(gst_no):
    """
    This function checks the validity of a given GST number by computing its check sum and comparing it with the last digit
    :param gst_no: The GST number that needs to be checked
    :type gst_no: str
    :return: Returns a string indicating whether the check sum matches or mismatches the last digit
    """

    last_digit = gst_no[-1]
    computed_check_sum = get_gst_check(gst_no[:-1])
    if computed_check_sum == last_digit:
        return "Check Sum MATCH"
    else:
        return "Check Sum MISMATCH"


def extract_pan(gst_no):
    """
    Extracts the PAN number from a GST number.

    Parameters:
    gst_no (str): The GST number from which the PAN number needs to be extracted.
                  The GST number must be at least 15 characters long.

    Returns:
    str: The extracted PAN number.

    Raises:
    TypeError: If the `gst_no` parameter is not a string.
    ValueError: If the `gst_no` parameter is not at least 15 characters long.
    """
    if not isinstance(gst_no, str):
        raise TypeError("The GST number must be a string.")

    if len(gst_no) < 15:
        raise ValueError("The GST number must be at least 15 characters long.")

    pan_num = gst_no[2:12]

    return pan_num




def get_gst_type(gst_no: str) -> str:
    """
    Identify the type of the given GST number and return a string describing the type.

    Args:
        gst_no: A string containing the GST number.

    Returns:
        A string that describes the type of the GST number.
        Possible values are:
        - "OIDAR ID GSTN"
        - "UN BODY GSTN"
        - "GOVT DEPT ID GSTN"
        - "NRI GSTN"
        - "TDS ID GSTN"
        - "TCS ID GSTN"
        - "Normal_Composition_ISD GSTIN"
        - "Invalid GSTN"

    Raises:
        TypeError: If the provided `gst_no` is not a string.

        Exception: If the length of the `gst_no` is not 15 characters.
    """
    if not isinstance(gst_no, str):
        raise TypeError("GST number must be a string.")

    if len(gst_no) != 15:
        raise Exception("GST number must be 15 characters long.")

    oidar_id = re.compile("[9][9][0-9]{2}[a-zA-Z]{3}[0-9]{5}[O][S][0-9a-zA-Z]{1}")
    unbody = re.compile("[0-9]{4}[A-Z]{3}[0-9]{5}[UO]{1}[N][A-Z0-9]{1}")
    govt_depid = re.compile("[0-9]{2}[a-zA-Z]{4}[0-9]{5}[a-zA-Z]{1}[0-9]{1}[Z]{1}[0-9]{1}")
    nri_id = re.compile("[0-9]{4}[a-zA-Z]{3}[0-9]{5}[N][R][0-9a-zA-Z]{1}")
    tds_id = re.compile("[0-9]{2}[a-zA-Z]{4}[a-zA-Z0-9]{1}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[D]{1}[0-9a-zA-Z]{1}")
    tcs_id = re.compile("[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[C]{1}[0-9a-zA-Z]{1}")
    norm_com_isd = re.compile("[0-9]{2}[a-zA-Z]{5}[0-9]{4}[a-zA-Z]{1}[1-9A-Za-z]{1}[Zz1-9A-Ja-j]{1}[0-9a-zA-Z]{1}")

    if gst_no[-1] != get_gst_check(gst_no):
        return "Invalid GSTN"
    elif oidar_id.search(gst_no):
        return "OIDAR ID GSTN"
    elif unbody.search(gst_no):
        return "UN BODY GSTN"
    elif govt_depid.search(gst_no):
        return "GOVT DEPT ID GSTN"
    elif nri_id.search(gst_no):
        return "NRI GSTN"
    elif tds_id.search(gst_no):
        return "TDS ID GSTN"
    elif tcs_id.search(gst_no):
        return "TCS ID GSTN"
    elif norm_com_isd.search(gst_no):
        return "Normal_Composition_ISD GSTIN"
    else:
        return "Could not verify GSTN"


def process_gst_list(gst_list):
    """
    This function accepts a list of GST numbers, checks if they are valid, extracts their PAN numbers and identifies
    their type of GSTIN. It returns a pandas dataframe with the columns 'GSTIN', 'Valid', 'PAN Number', and 'GST Type'.
    :param gst_list: A list of GST numbers
    :return: A pandas dataframe with the columns 'GSTIN', 'Valid', 'PAN Number', and 'GST Type'
    """
    # Initialize an empty list to store dataframes
    dfs = []

    # Iterate through each element in the list
    for gst_no in gst_list:

        # Check if the GST number is valid
        is_valid = gstchecksum(gst_no)

        # Extract PAN number from the GST number
        pan_num = extract_pan(gst_no)

        # Identify the type of GSTIN
        gst_type = get_gst_type(gst_no)

        # Create a dataframe with the current row data
        current_df = pd.DataFrame({'GSTIN': [gst_no], 'Validity': [is_valid], 'PAN Number': [pan_num], 'GST Type': [gst_type]})

        # Append the dataframe to the list
        dfs.append(current_df)

    # Concatenate all the dataframes in the list
    df = pd.concat(dfs, ignore_index=True)

    return df


# df=process_gst_list("10AAACI1681G1Z4")

# print(df)

