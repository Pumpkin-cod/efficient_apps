  
def word_to_pdf(filepath):
    
    
    """
    A very simple funtion to covert the word file into pdf file
    
    This will take just one parameter i.e the file pah
    
    """
    
    from docx2pdf import convert
    
    print(f"The file {filepath} has been selected.")
    
    convert(filepath)
    

    print("The conversion has been completed.")
    
