import pandas as pd
import warnings
import json
from openpyxl import load_workbook
import os
from utilities.CONSTANTS2 import R1_JSON_COL_MAPPING


def flatten_dict(dict_obj):
    """
    This function flattens a nested dictionary consisting of lists and/or nested dictionaries.

    Parameters:
    dict_obj (dict): The dictionary to be flattened.

    Returns:
    dict: The flattened dictionary.
    """
    warnings.filterwarnings('ignore')

    flat_dict = {}
    for key, value in dict_obj.items():
        if isinstance(value, dict):
            flat_dict.update(flatten_dict(value))
        elif isinstance(value, list):
            if len(value) == 1:
                a = value[0]
                b = flatten_dict(a)
                flat_dict.update(b)
            elif len(value) > 1:
                flat_dict.update(expand_list(value))
        else:
            flat_dict[key] = value

    return flat_dict


def expand_list(list_obj):
    """
    This function expands a nested list consisting of lists and/or nested dictionaries.

    Parameters:
    list_obj (list): The list to be expanded.

    Returns:
    dict: The expanded dictionary.
    """
    import pandas as pd
    import warnings

    warnings.filterwarnings('ignore')

    conv_dict = {}

    if len(list_obj) == 1:
        a = list_obj[0]
        b = flatten_dict(a)
        conv_dict = b
    else:
        df2 = pd.DataFrame()
        for i in list_obj:
            if isinstance(i, dict):
                flat_dictl = flatten_dict(i)
                try:
                    df1 = pd.DataFrame(flat_dictl)
                except:
                    df1 = pd.DataFrame([flat_dictl])
                df2 = pd.concat([df2, df1], ignore_index=True)

            elif isinstance(i, list):
                a = expand_list(i)
                df2 = pd.concat([df2, pd.DataFrame([a])], ignore_index=True)

            else:
                dict_whole = {i: list_obj[i]}
                df1 = pd.DataFrame([dict_whole])
                df2 = pd.concat([df2, df1], ignore_index=True)

        conv_dict = df2.to_dict(orient="list")

    return conv_dict


def rename_r1_columns(dataframe):
    
    df_copy=dataframe
    df_copy.rename(columns=R1_JSON_COL_MAPPING,inplace=True)
    
    return df_copy


def gstr_table_wise(i,data,filepath,name):
    table_data = data[i]
    dic_table = expand_list(table_data)
    
    try:
        df = pd.DataFrame(dic_table)
    except ValueError:
        df = pd.DataFrame(dic_table, index=[0])


    df["GSTR1-Table"] = name
    df["Json File Name"] = filepath
                
    return df


def gstr1_to_excel(filepath):

    warnings.filterwarnings('ignore')

    print(f'The Json GSTR-1 file path selected is {filepath}')
    print("We are analyzing the sheets available")

    # extra line added in 10-05-2023 --
    def temp_formatter(file_path):
        if "Gstr1JsonToExcel" in file_path:
            return file_path.replace("Gstr1JsonToExcel", "")
    # end extra line added in 10-05-2023 --  
     
    folder=os.path.dirname(filepath)
    
    # fullpath1=folder+"\\"+"GSTR-1 Table Wise_"+ temp_formatter(filepath).split("\\")[-1].split(".")[0]+".xlsx"
    fullpath1=folder+"\\"+ temp_formatter(filepath).split("\\")[-1].split(".")[0]+".xlsx"
    print(fullpath1,"fullpath1\n\n\n\n\n\n")

    writer = pd.ExcelWriter(fullpath1, engine='xlsxwriter') #, options={'strings_to_formulas': True}

    with open(filepath) as json_file:
        data = json.load(json_file)

    dic_keys = data.keys

    df_b2b=pd.DataFrame()
    df_b2cl=pd.DataFrame()
    df_cdnr=pd.DataFrame()
    df_exp=pd.DataFrame()
    
    df_all_combined=pd.DataFrame()

    for i in dic_keys():
        if i == "b2b":
            print("Fetching the B2B data, Please wait for some time...!!")
            df_b2b=gstr_table_wise(i,data,filepath,name="B2B")
            df_b2b.to_excel(writer, sheet_name="B2B", index=False)
            df_all_combined=pd.concat([df_b2b])

        elif i == "b2cl":
            print("Fetching the B2CL data, Please wait for some time...!!")
            df_b2cl=gstr_table_wise(i,data,filepath,name="B2CL")
            df_b2cl.to_excel(writer, sheet_name="B2CL", index=False)
            df_all_combined=pd.concat([df_b2cl])

        elif i == "cdnr":
            print("Fetching the CDNR data, Please wait for some time...!!")
            df_cdnr=gstr_table_wise(i,data,filepath,name="CDNR")
            df_cdnr.to_excel(writer, sheet_name="CDNR", index=False)
            df_all_combined=pd.concat([df_cdnr])


        elif i == "exp":
            print("Fetching the Export data, Please wait for some time...!!")
            df_exp=gstr_table_wise(i,data,filepath,name="EXPORT")
            df_exp.to_excel(writer, sheet_name="EXPORT", index=False)
            df_all_combined=pd.concat([df_exp])
            
        else:
            add_case = data[i]
            
            if isinstance(add_case, list):
                dic_add_case = expand_list(add_case)

                try:
                    df_add_case = pd.DataFrame(dic_add_case)
                except ValueError:
                    df_add_case = pd.DataFrame(dic_add_case, index=[0])

                df_add_case["GSTR1-Table"] = i
                df_add_case.to_excel(writer, sheet_name=i, index=False)
            
            elif isinstance(add_case, dict):
                dic_add_case = flatten_dict(add_case)

                try:
                    df_add_case = pd.DataFrame(dic_add_case)
                except ValueError:
                    df_add_case = pd.DataFrame(dic_add_case, index=[0])

                df_add_case["GSTR1-Table"] = i
                df_add_case.to_excel(writer, sheet_name=i, index=False)
            else:
                pass

    print(data.keys())
    
    print("Consolidating All Major Tables in Single Sheet for you..!!")   
    
    df_all_combined=pd.concat([df_b2b,df_b2cl,df_cdnr,df_exp])
    df_all_combined=rename_r1_columns(df_all_combined)

    df_all_combined.to_excel(writer, sheet_name="effcorp_all_combined", index=False)
    # writer.save()
    print("All Data have been extracted Successfully! ")
    writer.close()
    print(f'The Excel Files are Extracted and kept in the below path\n{fullpath1}\n\n ')

    # return(writer)
    return{
            "all_combined": writer
        }

# gstr1_to_excel(r"C:\Users\Dell\Downloads\returns_11052021_R1_20AAACI1681G3Z1_offline_others_0.json")