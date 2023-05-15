import os
import glob
import pandas as pd
import numpy as np
import datetime

from utilities.CONSTANTS2 import R2A_B2B_COL_MAPPING, R2A_B2BA_COL_MAPPING,R2A_CDNR_COL_MAPPING,R2A_CDNRA_COL_MAPPING


def get_pan_number(x):
    if isinstance(x, str):
        return x[2:12:1]
    else:
        return ''


# def validate_files(folder):
#     # """
#     # Validates files in the specified folder, ensuring that all files have a .xlsx extension,
#     # the combined size of all files does not exceed 300 MB, and no single file exceeds 30 MB in size.
#     # :param folder: The folder containing the files to be validated.
#     # :return: None.
#     # """
    
#     # if folder.endswith("xlsx"):
#     #     folder = os.path.dirname(folder)
    
#     # filenames = glob.glob(os.path.join(folder, '*.xlsx'))
#     # total_size = sum(os.path.getsize(file) for file in filenames)
#     # if any(not file.endswith('.xlsx') for file in filenames):
#     #     raise ValueError('All files in the folder must have a .xlsx extension')
#     # elif total_size > 314572800:
#     #     raise ValueError('Combined file size for all files is more than 300 MB. Please use smaller files')
#     # elif any(os.path.getsize(file) > 31457280 for file in filenames):
#     #     raise ValueError('Single file size should not exceed 30 MB')


def read_excel_files(file_list):
    # file_name=file_list[0]
    # if folder_path:
    #     folder_path = os.path.dirname(folder_path)
    # excel_files = []
    # for file in file_list:
    #     print(file)
    #     if file.endswith(".xlsx") and "r2a" in file.lower():
    #         file_path = os.path.join(root, file)
    #         try:
    #             validate_files(file_path)
    #             excel_files.append(file_path)
    #         except ValueError as e:
    #             print(e)
    return file_list


def read_excel_sheet(excel_file, sheet_index, skip_rows):
    df = pd.read_excel(excel_file, sheet_name=sheet_index, skiprows=skip_rows)
    df.dropna(how="all",inplace=True)
    df['File_name'] = os.path.basename(excel_file)
    return df


def clean_add_cols_df(df2, tran_type="B2B"):

    df3=df2.copy()

    filt = df3['Final_Invoice_CNDN_No'].str.contains('Total', na=False)
    df3 = df3.loc[~filt]

    df3.loc[:, 'Inv_CN_DN_Date_Text'] = df3['Final_Invoice_CNDN_Date'].str.replace("-", ".")
    df3.loc[:, 'Total_Tax'] = df3['IGST_Amount'] + df3['CGST_Amount'] + df3['SGST_Amount']
    df3.loc[:, 'Unique_ID'] = df3['GSTIN_of_Supplier'] + "/" + df3['Final_Invoice_CNDN_No'] + "/" + df3['Inv_CN_DN_Date_Text']

    df3.loc[:, 'PAN_Number'] = df3["GSTIN_of_Supplier"].apply(get_pan_number)

    df3['GSTR2A_Table'] = tran_type

    df3.replace(np.nan, "", inplace=True, regex=True)

    return df3


def add_master_cols(df10):

    df10 = df10.replace(np.nan, "", regex=True)

    df10["Ultimate_Unique"] = df10["GSTR2A_Table"] + "/" + df10["Supply_Attract_Reverse_Charge"] + df10[
        "GSTR_1_5_Filing_Status"] + "/" + df10["Unique_ID"]

    
    #this concatanating for B2BA cases, does nt require to use np.where coz we have now recitifed and kept as Final& Jnitial
    
    df10["PAN_3_Way_Key"] = np.where(df10["GSTR2A_Table"] == "B2BA",
                                     df10["PAN_Number"] + "/" + df10["Final_Invoice_CNDN_No"] + "/"
                                     + df10["Inv_CN_DN_Date_Text"],
                                     df10["PAN_Number"] + "/" + df10["Final_Invoice_CNDN_No"]
                                     + "/" + df10["Inv_CN_DN_Date_Text"])

    df10["PAN_2_Way_Key_PAN_InvNo"] = np.where(df10["GSTR2A_Table"] == "B2BA",
                                               df10["PAN_Number"] + "/" + df10["Final_Invoice_CNDN_No"]
                                               , df10["PAN_Number"] + "/" + df10["Final_Invoice_CNDN_No"])

    df10["PAN_2_Way_Key_PAN_InvDt"] = np.where(df10["GSTR2A_Table"] == "B2BA",
                                               df10["PAN_Number"] + "/" + df10["Inv_CN_DN_Date_Text"]
                                               , df10["PAN_Number"] + "/" + df10["Inv_CN_DN_Date_Text"])

    return df10


def gstr2a_merge(file_list):
    """
    Merge all the GSTR2A files in a folder.

    :param folder_path: The path to the folder containing the GSTR2A files to be merged.
    :return: A merged Excel file containing all the B2B, B2BA, CDNR, and CDNRA sheets.
    """
    excel_files = file_list
    print(f"The files that will be combined are:\n{excel_files}")

    print("We are combining the B2B sheets of all files...")
    df_b2b = pd.concat([read_excel_sheet(file, 1, [0, 1, 2, 3, 4]) for file in excel_files])
    
    print("We are combining the B2BA sheets of all files...")
    df_b2ba = pd.concat([read_excel_sheet(file, 2, [0, 1, 2, 3, 4, 5]) for file in excel_files])
    
    print("We are combining the CDNR sheets of all files...")
    df_cdnr = pd.concat([read_excel_sheet(file, 3, [0, 1, 2, 3, 4]) for file in excel_files])
    
    print("We are combining the CDNRA sheets of all files...")
    df_cdnra = pd.concat([read_excel_sheet(file, 4, [0, 1, 2, 3, 4, 5]) for file in excel_files])


    print("Renaming the Column Names...")
    df_b2b.rename(columns=R2A_B2B_COL_MAPPING, inplace=True)
    df_b2ba.rename(columns=R2A_B2BA_COL_MAPPING, inplace=True)
    df_cdnr.rename(columns=R2A_CDNR_COL_MAPPING, inplace=True)
    df_cdnra.rename(columns=R2A_CDNRA_COL_MAPPING, inplace=True)

    print("Cleaning the data and adding columns...")
    final_b2b=clean_add_cols_df(df_b2b,tran_type="B2B")
    final_b2ba=clean_add_cols_df(df_b2ba,tran_type="B2BA")
    final_cdnr=clean_add_cols_df(df_cdnr,tran_type="CDNR")
    final_cdnra=clean_add_cols_df(df_cdnra,tran_type="CDNRA")

    
    all_sheets = [final_b2b, final_b2ba, final_cdnr, final_cdnra]
    
    print("Merging all the sheets created...")
    df_all = pd.concat(all_sheets)
    df_all.reset_index(inplace=True, drop=True)
    
    df_all_added=add_master_cols(df_all)
    
    print("The File is ready to download...")

    timestamp=datetime.datetime.now().strftime("%d%m%Y%H%M%S")

    final_file=os.path.join(os.path.dirname(file_list[0]),"GSTR2A_Combined_file_"+timestamp+".xlsx")
    print(final_file)
    df_all_added.to_excel(final_file,index=False)

    # return df_all_added
    return {
            "all_combined": final_file
        }



# df=gstr2a_merge(r"D:\My Drive\Eff Corp Website\GSTR2A ITR RECO\Exercise_19032023_0815\TEST GSTR2A")

# df.to_excel("Outheck.xlsx")



