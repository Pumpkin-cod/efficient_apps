import os
import tempfile
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter


def addnumber_pdf(filepath):
    """
    This function is used for adding the page Number at the bottom of the pdf file.
    We only need to provide one parameter, i.e the complete file path to the pdf file.
    The function will return a separate pdf with suffix as _numbers and this pdf file will be stored in the same location.
    """

    print("Code developed by SHUBHAM: GitHub Account 26Shubham")

    tmp_file = None
    try:
        # Create a temporary PDF file with page numbers
        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_file:
            create_pdfpage(PdfFileReader(filepath).getNumPages(), tmp_file.name)

        # Merge page numbers with original PDF file
        output = PdfFileWriter()
        with open(filepath, 'rb') as pdf_file, open(tmp_file.name, 'rb') as num_file:
            pdf = PdfFileReader(pdf_file, strict=False)
            num_pdf = PdfFileReader(num_file, strict=False)
            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                num_page = num_pdf.getPage(i)
                page.mergePage(num_page)
                output.addPage(page)

            # Save output PDF file
            folder = Path(filepath).parent
            new_file = folder / (Path(filepath).stem + "_numbered.pdf")
            with open(new_file, 'wb') as f:
                output.write(f)
            print(f"The page number has been added in {filepath} and this numbered pdf has been saved as {new_file}")

    finally:
        if tmp_file:
            os.remove(tmp_file.name)
