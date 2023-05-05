import win32com.client as client
import os


def excel_to_pdf(filepath, sheet=1):
    """
    This function will convert the excel file into a PDF file.
    Please ensure that the content in the excel is within the printable area.
    :param filepath: complete file path to the Excel file
    :param sheet: sheet number or sheet name (optional, default is the first sheet)
    """
    print(f"Code developed by SHUBHAM: Git Hub Account 26Shubham\n")

    # extract file and folder names
    original_file = os.path.basename(filepath)
    folder = os.path.dirname(filepath)

    # open Excel application and the workbook
    excel = client.Dispatch("Excel.Application")
    wb = excel.Workbooks.Open(filepath)

    # get the sheet by name or index
    if isinstance(sheet, int):
        ws = wb.Worksheets[sheet-1]
    elif isinstance(sheet, str):
        ws = wb.Worksheets[sheet]
    else:
        print("Invalid sheet parameter, please specify sheet number or sheet name.")
        return

    # create the output PDF file name
    pdf_name = f"{os.path.splitext(original_file)[0]}_pdf_converted.pdf"
    pdf_path = os.path.join(folder, pdf_name)

    # export the sheet as PDF
    ws.ExportAsFixedFormat(0, pdf_path)

    # close workbook and Excel application
    wb.Close()
    excel.Quit()

    print(f"The Excel file '{original_file}' has been converted to PDF: '{pdf_name}'\n")
