import os
import PyPDF2
from getpass import getpass

def encrypt_pdf(filepath, password="Password@1", type="function"):
    """
    This function is for setting the password in any pdf file.
    There are two ways of setting the password.
    We can provide a complete filepath and also provide a password we want to set.

    Input Parameters are as below:

    filepath: The complete path to the file needs to be provided.
    password: This is an optional parameter. By default, the password will be set as "Password@1".
              It is highly recommended not to use the default password and set your own value inside the password.
    type: Default value is function. This need not be changed unless you want the user to provide the password.
          If the user will provide the password, then select type as "user". This will prompt an input box,
          and the user will have to enter the password in the input box.

    Output will be stored in the same folder as the original pdf file.
    The name of the pdf file will remain the same, only the _encrypted will be added at the last.
    """
    
    print("Code developed by SHUBHAM: Git Hub Account 26Shubham")

    if type == "function":
        # Read the pdf file and create a writer object
        with open(filepath, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            pdf_writer = PyPDF2.PdfFileWriter()

            # Add all pages to writer
            for page_num in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(page_num))

            # Encrypt with the provided password
            pdf_writer.encrypt(password)

            # Write the output file
            folder = os.path.dirname(filepath)
            filename = os.path.join(folder, os.path.splitext(os.path.basename(filepath))[0] + "_encrypted.pdf")

            with open(filename, 'wb') as output_file:
                pdf_writer.write(output_file)

            print(f"The file {os.path.basename(filepath)} has been encrypted and stored in the same folder.")
            return output_file

    elif type == "user":
        original_file = os.path.basename(filepath)

        # Prompt user to enter password
        print(f"The file {original_file} has been selected. What password do you want to set?")
        file_pass = getpass("Enter the Password for this pdf File")

        # Call this function again with the provided password
        encrypt_pdf(filepath, password=file_pass, type="function")

        print("The Password has been set.")
    else:
        print("Some Error in Inputs given. Please Check Documentation.")
