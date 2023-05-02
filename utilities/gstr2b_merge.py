import os
import glob
import pandas as pd
import numpy as np

def validate_files(folder):
    """
    Validates files in the specified folder, ensuring that all files have a .xlsx extension,
    the combined size of all files does not exceed 300 MB, and no single file exceeds 30 MB in size.
    :param folder: The folder containing the files to be validated.
    :return: None.
    """
    
    if folder.endswith("xlsx"):
        folder = os.path.dirname(folder)
    
    filenames = glob.glob(os.path.join(folder, '*.xlsx'))
    total_size = sum(os.path.getsize(file) for file in filenames)
    if any(not file.endswith('.xlsx') for file in filenames):
        raise ValueError('All files in the folder must have a .xlsx extension')
    elif total_size > 314572800:
        raise ValueError('Combined file size for all files is more than 300 MB. Please use smaller files')
    elif any(os.path.getsize(file) > 31457280 for file in filenames):
        raise ValueError('Single file size should not exceed 30 MB')


def read_excel_files(folder_path):
    if folder_path.endswith("xlsx"):
        folder_path = os.path.dirname(folder_path)
    excel_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            print(file)
            if file.endswith(".xlsx") and "r2b" in file.lower():
                file_path = os.path.join(root, file)
                try:
                    validate_files(file_path)
                    excel_files.append(file_path)
                except ValueError as e:
                    print(e)
    return excel_files


def process_excel_sheets(filepath,sheet_name,drop_cols,rename_col_mapping):
    df=pd.read_excel(filepath,sheet_name =sheet_name)
    df.rename(rename_col_mapping)
    




