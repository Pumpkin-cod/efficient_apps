import os
import comtypes.client

def ppt_to_pdf(filepath):
    """
    This function will convert each slide of your PPT into a PDF file.
    Only one parameter needs to be given, i.e the Complete Path to the PPT File.
    The output PDF file will have the same name as Input file and will be stored in the same folder.
    """
    print("Code developed by SHUBHAM: GitHub Account 26Shubham")
    
    print("Your Input file is at:")
    print(filepath)

    outputFilePath = os.path.splitext(filepath)[0] + ".pdf"

    print("Your Output file will be at:")
    print(outputFilePath)

    print("We are converting Your file, please Wait...!!")

    powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
    powerpoint.Visible = 1

    slides = powerpoint.Presentations.Open(filepath)

    slides.SaveAs(outputFilePath, 32)

    slides.Close()

    powerpoint.Quit()

    print("The PPT has been converted to PDF file successfully!")
