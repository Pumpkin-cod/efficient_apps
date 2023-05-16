import pandas as pd
import warnings
import json
from openpyxl import load_workbook
import os
from utilities.CONSTANTS2 import R2B_JSON_COL_MAPPING
from utilities.gstr1_to_excel import flatten_dict, expand_list


def rename_r2b_columns(dataframe):
    
    df_copy=dataframe
    df_copy.rename(columns=R2B_JSON_COL_MAPPING,inplace=True)
    
    return df_copy


def gstr_table_wise(i,data,filepath,return_period,rec_gstin):

    table_data = data[i]
    dic_table = expand_list(table_data)
    df = pd.DataFrame(dic_table)
    # df = pd.DataFrame(dic_table, index=[0])
    
    try:
        df = pd.DataFrame(dic_table)
    except ValueError:
        df = pd.DataFrame(dic_table, index=[0])


    df["GSTR1-Table"] = i
    df["rtnprd"]=return_period
    df["gstin"]=rec_gstin
    df["Json File Name"]=filepath
    
    return df


def gstr2b_to_excel(filepath):
    """
    This is a very easy to use funcion to extract the json data of GSTR2b into an excel file.
    This function takes only one argument i.e a completepath to the json file upto extension
    Simply pass the complete path and run.
    Table wise data will be populated in the Excel sheet
    """
    warnings.filterwarnings('ignore')

    original_name=os.path.basename(filepath)
    original_filename=original_name.split(".")[0]
    original_file_ext=original_name.split(".")[1]
    folder = os.path.dirname(filepath)
    newfile = os.path.join(folder,"Converted_Excel_GSTR2B.xlsx")


    print(newfile)

    print(f"the file {original_name} has been selected... Working on it..!")
    writer = pd.ExcelWriter(newfile, engine='xlsxwriter') #, options={'strings_to_formulas': True}

    #creating empty dataframe to avoid any error

    df_impg=pd.DataFrame()
    df_isd=pd.DataFrame()
    df_cdnr=pd.DataFrame()
    df_cdnra=pd.DataFrame()
    df_b2b=pd.DataFrame()
    df_b2ba=pd.DataFrame()
    df_all_combined=pd.DataFrame()

    with open(filepath) as json_file:
        data = json.load(json_file)
        main_data=data["data"]['docdata']
        return_period=data["data"]["rtnprd"]
        rec_gstin=data["data"]["gstin"]

        for i in main_data.keys():
            if i =="b2b":

                print(f"Fetching the {i} data, Please wait for some time...!!")
                df_b2b=gstr_table_wise(i,main_data,filepath,return_period,rec_gstin)   
                df_b2b.to_excel(writer, sheet_name=str(i+'_data'), index=False)

            elif i=="b2ba":

                print(f"Fetching the {i} data, Please wait for some time...!!")
                df_b2ba=gstr_table_wise(i,main_data,filepath,return_period,rec_gstin)                
                df_b2ba.to_excel(writer, sheet_name=str(i+'_data'), index=False)

            elif i=="cdnr":
                print(f"Fetching the {i} data, Please wait for some time...!!")
                df_cdnra=gstr_table_wise(i,main_data,filepath,return_period,rec_gstin)                
                df_cdnr.to_excel(writer, sheet_name=str(i+'_data'), index=False)       
                

            elif i=="cdnra":
                print(f"Fetching the {i} data, Please wait for some time...!!")
                df_cdnra=gstr_table_wise(i,main_data,filepath,return_period,rec_gstin)                
                df_cdnra.to_excel(writer, sheet_name=str(i+'_data'), index=False)
                
            elif i=="isd":
                print(f"Fetching the {i} data, Please wait for some time...!!")
                df_isd=gstr_table_wise(i,main_data,filepath,return_period,rec_gstin)                
                df_isd.to_excel(writer, sheet_name=str(i+'_data'), index=False)

            elif i=="impg":
                print(f"Fetching the {i} data, Please wait for some time...!!")
                df_impg=gstr_table_wise(i,main_data,filepath,return_period,rec_gstin)                
                df_impg.to_excel(writer, sheet_name=str(i+'_data'), index=False)

        print(f"All Sheets Have been created separately in same Excel File named {newfile}")


    combined_2b=pd.concat([df_b2b,df_b2ba,df_cdnr,df_cdnra,df_isd,df_impg])

    print("Combining all sheets into one single Excel Sheet , Named 'effcorp_all_combined'")

    combined_2b.to_excel(writer,sheet_name="effcorp_all_combined",index=False)

    print(f"Please Wait...Saving the single final file as {newfile}")

    # writer.save()
    writer.close()

    # return (writer)
    return{"all_combined": writer}


# df=gstr2b_to_excel(r"C:\Users\Dell\Downloads\Json file\CXDPK2766F2ZS_092021_GSTR2B_20220112.json")

# df.to_excel("output.xlsx")