def rotate_pdf(filepath, rotation_type="normal", degree=0, odd_degree=0, even_degree=0):
    """
    This function is used for rotating the pages of a PDF file.

    Parameters:
    - filepath: str - The complete file path to the PDF file.
    - rotation_type: str - The type of rotation to be performed. The default value is "normal". Other possible values are "odd_even".
    - degree: int - The degree of rotation to be performed on the pages. The default value is 0.
    - odd_degree: int - The degree of rotation to be performed on the odd pages if rotation_type is "odd_even". The default value is 0.
    - even_degree: int - The degree of rotation to be performed on the even pages if rotation_type is "odd_even". The default value is 0.

    The function will create a new PDF file with the rotated pages and save it in the same location with a suffix as "_rotated".
    """

    print("Code developed by PRANAV: GitHub Account pranav7712")

    original_file = os.path.basename(filepath)

    with open(filepath, 'rb') as f:
        pdf = PdfFileReader(f)
        writer = PdfFileWriter()

        if rotation_type == "normal":
            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                page.rotateClockwise(degree)
                writer.addPage(page)

            print(f"All pages of the file {original_file} have been rotated at {degree} degrees.")

        elif rotation_type == "odd_even":
            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                if (i + 1) % 2 == 0:
                    page.rotateClockwise(even_degree)
                else:
                    page.rotateClockwise(odd_degree)
                writer.addPage(page)

            print(f"Odd pages of the file {original_file} have been rotated at {odd_degree} degrees and even pages at {even_degree} degrees.")

        else:
            print("Specify the correct rotation type.")

        folder = os.path.dirname(filepath)
        new_file = os.path.join(folder, f"{os.path.splitext(original_file)[0]}_rotated.pdf")

        with open(new_file, 'wb') as output:
            writer.write(output)

        print(f"The file has been rotated and saved as {new_file}.")
