import pandas as pd
import os
from shutil import copyfile


def split_excel(filepath, cols, sheet=0, mode="file"):
    """
    This function splits the data in an excel file based on the unique values in a given column.
    The output can either be stored in separate files (mode="file") or separate sheets in a new excel file (mode="sheets").
    """

    # Read the data from the excel file
    df = pd.read_excel(filepath, sheet_name=sheet)

    # Get a list of unique values in the specified column
    cols_list = list(set(df[cols].values))

    if mode == "file":
        # Split data into separate excel files based on column values
        for i in cols_list:
            # Create new file for each unique column value
            new_file = os.path.join(os.path.dirname(filepath), f"{i}.xlsx")
            # Write data to the new file
            df[df[cols] == i].to_excel(new_file, sheet_name=i[0:25:1], index=False)

        print(f"Your data has been split into {len(cols_list)} files based on {cols} column.")
        print(f"All the files are stored in the same folder as the input file: {os.path.dirname(filepath)}")

    elif mode == "sheets":
        # Split data into separate sheets in a new excel file based on column values
        extension = os.path.splitext(filepath)[1]
        filename = os.path.splitext(filepath)[0]
        new_file = os.path.join(os.path.dirname(filepath), f"{filename}_Sheet_Split_Auto{extension}")

        # Copy original file to new file
        copyfile(filepath, new_file)

        # Write each unique column value to a separate sheet in the new file
        writer = pd.ExcelWriter(new_file, engine='openpyxl')
        for myname in cols_list:
            mydf = df.loc[df[cols] == myname]
            mydf.to_excel(writer, sheet_name=str(myname[0:25:1]), index=False)
        writer.save()

        print(f"Your data has been split into {len(cols_list)} sheets based on {cols} column.")
        print(f"The output excel file with all these sheets is stored in {new_file}")

    else:
        print("Invalid mode specified.")
