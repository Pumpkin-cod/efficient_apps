import glob
import os
import pandas as pd


def combine_excel(folder, mode="file", sheet=0):
    """
    Combine Excel files or sheets into a single Excel file.

    Parameters:
    folder (str): Folder path containing the Excel files or file path of the Excel file containing sheets.
    mode (str): Mode of combining. Default is "file". Can be "file" or "sheets".
    sheet (str, int): Sheet name or index to read. Default is 0.

    Returns:
    None
    """
    if mode == "file":
        files = glob.glob(os.path.join(folder, "*.xls*"))
        if not files:
            print("No Excel files found in the specified folder.")
            return
        df = pd.concat((pd.read_excel(f, sheet_name=sheet).assign(File_Name=f) for f in files),
                       ignore_index=True, sort=False)
        newfile = os.path.join(folder, "All_ExcelFiles_Combined_Auto.xlsx")
        df.to_excel(newfile, sheet_name="Combined", index=False)
        print(f"All the files in the folder {folder} have been combined into a single Excel File. "
              f"\n\nThe Combined Excel File stored in {newfile}")
    elif mode == "sheets":
        if not os.path.isfile(folder):
            print("Specified path is not a valid file path.")
            return
        pth = os.path.dirname(folder)
        xl = pd.ExcelFile(folder)
        if sheet not in xl.sheet_names:
            print(f"Sheet {sheet} not found in the Excel file.")
            return
        df = pd.concat((pd.read_excel(folder, sheet_name=s).assign(Sheet_Name=s) for s in xl.sheet_names),
                       ignore_index=True, sort=False)
        newfile = os.path.join(pth, f"All_Sheets_Combined_Auto_{sheet}.xlsx")
        df.to_excel(newfile, sheet_name="Combined", index=False)
        print(f"All the sheets in the Excel file {folder} have been combined into a single sheet named 'Combined'. "
              f"\n\nThe New Excel File is stored in {newfile}")
    else:
        print("Invalid mode specified.")


if __name__ == "__main__":
    combine_excel("/path/to/folder", mode="file")
    combine_excel("/path/to/file.xlsx", mode="sheets", sheet="Sheet1")
