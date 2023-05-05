from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def delete_pdfpage(filepath):

    infile = PdfFileReader(filepath, 'rb')
    output = PdfFileWriter()
    total_page = infile.getNumPages()
    original_file = os.path.basename(filepath)

    print(f"The pdf file {original_file} has been selected. It has total {total_page} number of pages")

    n = int(input("Enter how many pages you want to delete: "))
    pages_to_delete = list(map(int, input("\nEnter the page numbers (separated by spaces): ").strip().split()))[:n]
    pages_to_delete = [p-1 for p in pages_to_delete]

    if max(pages_to_delete) >= total_page:
        print("Error: Invalid page number")
        return

    new_file = os.path.join(os.path.dirname(filepath), f"{os.path.splitext(original_file)[0]}_deleted{os.path.splitext(original_file)[1]}")
        
    for i, page in enumerate(infile.pages):
        if i not in pages_to_delete:
            output.addPage(page)

    with open(new_file, 'wb') as f:
        output.write(f)

    print(f"Total {n} pages have been deleted. The new PDF has been stored in the same folder.")
