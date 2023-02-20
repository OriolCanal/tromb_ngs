import os
import pandas as pd
import subprocess
import re
from collections import Counter


def classificate_RB_project (excel_path):
    """ Given an excel file (RB first column, project second column)
        It creates a dictionary with rb_project[rb] : poject """
     

    cols = ["rb", "project", "run", "ox", "llibreta", "other1", "other2"]
    dataframe = pd.read_excel(excel_path, engine="openpyxl", names = cols, sheet_name="Mònica")
    print (dataframe)
    rb_project_dict = {}
    # dataframe.columns = cols

    for index, row in dataframe.iterrows():
        key = row["rb"].strip()
        print (key)
        value = row["project"].replace(" ", "_").upper()
        if key == "RB24839":
            value == "MOSCAT"
        rb_project_dict[key] = value
    return (rb_project_dict)

excel_path = "/home/ocanal/Escritorio/Trombosi/classification_samples_project.xlsx"



# Set the directory containing the subdirectories
parent_dir = '/home/ocanal/Escritorio/Trombosi'

def rivero_vcf_to_folder(rb_project_dict, parent_dir):

    ID_regex_exp = "[A-Z]{2}[0-9]{5}"
    output_directory = f"{parent_dir}/Rivero_vcf/"

    list = []
    ID_list = []
    if not os.path.exists(output_directory):
        os.mkdir(output_directory)

    # Iterate over the subdirectories
    for subdir in os.listdir(parent_dir):
        subdir_path = os.path.join(parent_dir, subdir)

        # Check if the current item is a directory
        if os.path.isdir(subdir_path):
            # Check if the subdirectory contains an "Excel" directory
            vcf_dir_path = os.path.join(subdir_path, 'vcf')
            if os.path.isdir(vcf_dir_path):
                # Iterate over the Excel files in the excels directory
                for file in os.listdir(vcf_dir_path):
                    vcf_file = os.path.join(vcf_dir_path, file)
                    
                    # Check if the file is an Excel file
                    ID = re.search(ID_regex_exp, file).group(0)
                    if ID not in ID_list:
                        ID_list.append(ID)
                        project = rb_project_dict[ID]
                        #print (f"ID {ID}\n project {project}")
                        if project == "PROJECTE_DANI_RIVERO":
                            list.append(ID)
                            cmd = f"cp {vcf_dir_path}/*{ID}* {output_directory}"
                            subprocess.run(cmd, shell=True)
                            print (f"removing ID {ID}")
                            del rb_project_dict[ID]
    print(rb_project_dict)
    counter = Counter(list)
    result = [i for i, j in counter.items() if j > 1]
    #print(result)

    # for key,value in rb_project_dict.items():
    #     print(key, value)


rb_project_dict = classificate_RB_project(excel_path)
rivero_vcf_to_folder(rb_project_dict, parent_dir)