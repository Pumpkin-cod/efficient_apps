import pandas as pd
import glob
import os


def combine_txt(folder):
    
    # Print information about the developer
    print("Code developed by SHUBHAM: GitHub Account 26Shubham")
    
    # Define the output file name
    newfile = os.path.join(folder, 'Combined_Text_File_Auto.txt')

    # Get a list of all text files in the folder
    filenames = glob.glob(os.path.join(folder, '*.txt'))

    # Create an empty DataFrame to store the combined data
    df_combined = pd.DataFrame()

    # Loop over all text files and append them to the combined DataFrame
    for file in filenames:
        df = pd.read_csv(file, sep='\t', low_memory=False, encoding='cp1252')
        df_combined = df_combined.append(df)

    # Write the combined DataFrame to a new text file
    df_combined.to_csv(newfile, sep='\t', index=False)

    # Print a message to indicate the operation is completed
    print(f"All text files in the folder {folder} have been merged and stored in {newfile}")
