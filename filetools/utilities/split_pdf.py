import os
import math
from PyPDF2 import PdfFileReader, PdfFileWriter

def split_pdf(filepath, split_type="page_wise", split_set=1):
    print("Code developed by PRANAV: GitHub account pranav7712")

    with open(filepath, 'rb') as f:
        pdf = PdfFileReader(f)

        if split_type == "page_wise":
            for i in range(pdf.getNumPages()):
                writer = PdfFileWriter()
                writer.addPage(pdf.getPage(i))

                filename = os.path.splitext(os.path.basename(filepath))[0]
                newfile = os.path.join(os.path.dirname(filepath), f"{filename}_Page_{i+1}.pdf")
                with open(newfile, "wb") as output:
                    writer.write(output)
                print(f"The file has been saved as {newfile}")

        elif split_type == "cummulative":
            writer = PdfFileWriter()
            for i in range(0, pdf.getNumPages()):
                page = pdf.getPage(i)
                writer.addPage(page)

                filename = os.path.splitext(os.path.basename(filepath))[0]
                newfile = os.path.join(os.path.dirname(filepath), f"{filename}_Page_1-{i+1}.pdf")
                with open(newfile, "wb") as output:
                    writer.write(output)
                print(f"The file has been saved as {newfile}")

        elif split_type == "oddeven":
            writer1 = PdfFileWriter()
            writer2 = PdfFileWriter()
            for i in range(0, pdf.getNumPages()):
                page = pdf.getPage(i)
                if (i+1) % 2 == 0:
                    writer1.addPage(page)
                else:
                    writer2.addPage(page)

            filename = os.path.splitext(os.path.basename(filepath))[0]
            newfile_even = os.path.join(os.path.dirname(filepath), f"{filename}_Even Pages.pdf")
            newfile_odd = os.path.join(os.path.dirname(filepath), f"{filename}_Odd Pages.pdf")

            with open(newfile_even, "wb") as output_even, open(newfile_odd, "wb") as output_odd:
                writer1.write(output_even)
                writer2.write(output_odd)

            print(f"The files have been saved as {newfile_even} and {newfile_odd}")

        elif split_type == "ranges":
            tot_page = pdf.getNumPages()
            files = math.ceil(tot_page/split_set)
            a = 0
            for i in range(files):
                writer1 = PdfFileWriter()
                try:
                    for j in range(0, split_set):
                        page = pdf.getPage(a)
                        a += 1
                        writer1.addPage(page)

                    filename = os.path.splitext(os.path.basename(filepath))[0]
                    newfile = os.path.join(os.path.dirname(filepath), f"{filename}_Set_{i+1}.pdf")
                    with open(newfile, "wb") as output:
                        writer1.write(output)

                except IndexError:
                    for j in range(0, tot_page - a):
                        page = pdf.getPage(a)
                        a += 1
                        writer1.addPage(page)
                    filename = os.path.splitext(os.path.basename(filepath))[0]
                    newfile = os.path.join(os.path.dirname(filepath), f"{filename}_Set_{i+1}.pdf")
                    with open(newfile, "wb") as output:
                        writer1.write(output)

            print(f"{files} files were created successfully")
        
        elif split_type == "split_equal":
        tot_page = pdf.getNumPages()
        files = math.ceil(tot_page / split_set)
        for i in range(files):
            start_index = i * split_set
            end_index = min((i + 1) * split_set, tot_page)
            writer = PdfFileWriter()
            for j in range(start_index, end_index):
                page = pdf.getPage(j)
                writer.addPage(page)
            filename = os.path.splitext(os.path.basename(filepath))[0]
            newfile = os.path.join(os.path.dirname(filepath), f"{filename}_Set_{i+1}.pdf")
            with open(newfile, "wb") as output:
                writer.write(output)
            print(f"The file has been saved as {newfile}")
        
        else:
            print("Please check the input")

            
    return True
