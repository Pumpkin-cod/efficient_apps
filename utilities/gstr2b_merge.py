import os
import glob
import pandas as pd
import numpy as np
import datetime

from utilities.CONSTANTS2 import R2B_B2B_COL_MAPPING,R2B_B2BA_COL_MAPPING,R2B_CDNR_COL_MAPPING,R2B_CDNRA_COL_MAPPING,R2B_IMPG_COL_MAPPING,R2B_ISD_COL_MAPPING

# def validate_files(folder):
#     """
#     Validates files in the specified folder, ensuring that all files have a .xlsx extension,
#     the combined size of all files does not exceed 300 MB, and no single file exceeds 30 MB in size.
#     :param folder: The folder containing the files to be validated.
#     :return: None.
#     """
    
#     if folder.endswith("xlsx"):
#         folder = os.path.dirname(folder)
    
#     filenames = glob.glob(os.path.join(folder, '*.xlsx'))
#     total_size = sum(os.path.getsize(file) for file in filenames)
#     if any(not file.endswith('.xlsx') for file in filenames):
#         raise ValueError('All files in the folder must have a .xlsx extension')
#     elif total_size > 314572800:
#         raise ValueError('Combined file size for all files is more than 300 MB. Please use smaller files')
#     elif any(os.path.getsize(file) > 31457280 for file in filenames):
#         raise ValueError('Single file size should not exceed 30 MB')


# def read_excel_files(folder_path):
#     excel_files = []
#     for root, dirs, files in os.walk(folder_path):
#         for file in files:
#             print(file)
#             if file.endswith(".xlsx"):
#                 file_path = os.path.join(root, file)
#                 try:
#                     validate_files(file_path)
#                     excel_files.append(file_path)
#                 except ValueError as e:
#                     print(e)
#     return excel_files


def process_excel_sheets(filepath,sheet_name,drop_cols,rename_col_mapping):
    try:
        df=pd.read_excel(filepath,sheet_name =sheet_name)
        df =df.drop(drop_cols)
        df.rename(rename_col_mapping,axis=1,inplace=True)
        df['GSTR2B_Table']=sheet_name
        df['File_Name']=os.path.basename(filepath)
    except:
        df=pd.DataFrame()
    return df


def gstr2b_merge(file_list):
    """
    Merge all the GSTR2A files in a folder.

    :param folder_path: The path to the folder containing the GSTR2A files to be merged.
    :return: A merged Excel file containing all the B2B, B2BA, CDNR, and CDNRA sheets.
    """
    
    df_b2b=pd.DataFrame()
    df_b2ba=pd.DataFrame()
    df_cdnr=pd.DataFrame()
    df_cdnra=pd.DataFrame()
    df_isd=pd.DataFrame()
    df_impg=pd.DataFrame()

    excel_files = file_list
    print(f"The files that will be combined are:\n{excel_files}")

    print("We are combining the B2B sheets of all files...")
    df_b2b = pd.concat([process_excel_sheets(file, "B2B", [0, 1, 2, 3, 4],R2B_B2B_COL_MAPPING) for file in excel_files])

    
    print("We are combining the B2BA sheets of all files...")
    df_b2ba = pd.concat([process_excel_sheets(file, "B2BA", [0, 1, 2, 3, 4, 5],R2B_B2BA_COL_MAPPING) for file in excel_files])

    print("We are combining the CDNR sheets of all files...")
    df_cdnr = pd.concat([process_excel_sheets(file, "B2B-CDNR", [0, 1, 2, 3, 4],R2B_B2B_COL_MAPPING) for file in excel_files])
    
    print("We are combining the CDNRA sheets of all files...")
    df_cdnra = pd.concat([process_excel_sheets(file, "B2B-CDNRA", [0, 1, 2, 3, 4, 5],R2B_B2BA_COL_MAPPING) for file in excel_files])

    print("We are combining the ISD sheets of all files...")
    df_isd = pd.concat([process_excel_sheets(file, "ISD", [0, 1, 2, 3, 4],R2B_B2B_COL_MAPPING) for file in excel_files])
    
    print("We are combining the IMPG sheets of all files...")
    df_impg = pd.concat([process_excel_sheets(file, "IMPG", [0, 1, 2, 3, 4],R2B_B2BA_COL_MAPPING) for file in excel_files])
   
    all_sheets = [df_b2b, df_b2ba, df_cdnr, df_cdnra,df_isd,df_impg]
    
    print("Merging all the sheets created...")
    df_all = pd.concat(all_sheets)
    # df_all.reset_index(inplace=True, drop=True)
        
    print("The File is ready to download...")

    # return df_all
    timestamp=datetime.datetime.now().strftime("%d%m%Y%H%M%S")

    final_file=os.path.join(os.path.dirname(file_list[0]),"GSTR2B_Combined_file_"+timestamp+".xlsx")
    print(final_file)
    df_all.to_excel(final_file,index=False)

    # return df_all_added
    return {
            "all_combined": final_file
        }

# df=gstr2b_merge(r"D:\My Drive\Automation Adda\GENERAL PURPOSE RESOURCES\ALL GST RELATED FILES\GSTR2B EXCEL")

# df.to_excel("Output.xlsx")