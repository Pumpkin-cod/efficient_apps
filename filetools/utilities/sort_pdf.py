from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def sort_pdf(filepath):
    """
    This function is used to sort the pdf files in reverse order.
    Only One parameter is required i.e the Complete path to the file which is to be sorted.
    Output will be stored in the same folder as the original pdf file.
    The name of the pdf file will remain same, only the _sorted will be added at the last
    """
    print("Code developed by SHUBHAM : Git Hub Account 26Shubham")
    output_pdf = PdfFileWriter()
    original_file = os.path.basename(filepath)
    with open(filepath, 'rb') as readfile:
        input_pdf = PdfFileReader(readfile)
        for page in reversed(input_pdf.pages):
            output_pdf.addPage(page)
        folder = os.path.dirname(filepath)
        filename = os.path.join(folder, f"{os.path.splitext(original_file)[0]}_sorted.pdf")
        with open(filename, "wb") as writefile:
            output_pdf.write(writefile)
        print(f"The pdf file {original_file} has been sorted in reverse order and stored in the same folder as the original pdf file")
        return output_pdf
