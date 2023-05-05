import os
from getpass import getpass
from PyPDF2 import PdfFileReader, PdfFileWriter


def decrypt_pdf(filepath, password="Password@1", mode="function"):

    print("Code developed by SHUBHAM: GitHub Account 26Shubham")

    if mode == "function":
        folder = os.path.dirname(filepath)
        filename, ext = os.path.splitext(os.path.basename(filepath))

        output_path = os.path.join(folder, f"{filename}_decrypted{ext}")

        with open(filepath, "rb") as input_file, open(output_path, "wb") as output_file:
            reader = PdfFileReader(input_file)
            reader.decrypt(password)

            writer = PdfFileWriter()

            for page_num in range(reader.getNumPages()):
                page = reader.getPage(page_num)
                writer.addPage(page)

            writer.write(output_file)

        print(f"The file {filename}{ext} has been decrypted")

    elif mode == "user":
        filename = os.path.basename(filepath)

        print(f"The file {filename} has been selected. Enter the password to decrypt")

        file_pass = getpass("Enter the Password for this pdf File")

        decrypt_pdf(filepath, password=file_pass, mode="function")

        print("The file has been decrypted")

    else:
        print("Some error in inputs given. Please check documentation")
