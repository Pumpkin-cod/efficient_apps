import glob
import os
from PyPDF2 import PdfFileMerger, PdfFileReader
from fpdf import FPDF


def combine_pdf(folder, odd_even=False):
    '''
    This function is for combining multiple pdf files in a given folder.
    If odd_even is set to True, a blank page is added after each odd numbered pdf file,
    so that the combined document can be printed on both sides easily.
    '''

    print("Code developed by SHUBHAM : Git Hub Account 26Shubham")

    filenames = glob.glob(os.path.join(folder, "*.pdf"))
    merged = PdfFileMerger()

    if odd_even:
        pdf_blank = FPDF()
        pdf_blank.add_page()
        pdf_blank.output("Blankpage.pdf")

        g = open("Blankpage.pdf", 'rb')
        pdf_1 = PdfFileReader(g)

    for file in filenames:
        f = open(file, 'rb')
        pdf = PdfFileReader(f)
        
        if odd_even and (pdf.getNumPages() + 1) % 2 == 0:
            merged.append(pdf)
            merged.append(pdf_1)
            f.close()
        else:
            merged.append(pdf)
            f.close()

    if odd_even:
        g.close()
        os.remove("Blankpage.pdf")

    newfile = os.path.join(folder, 'Combined_Pdf_File_Auto.pdf')
    merged.write(newfile)
    merged.close()

    print(f"All pdf files in the selected folder have been merged and stored in {newfile}")

