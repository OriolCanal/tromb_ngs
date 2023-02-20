import os
import pandas as pd

# Set the directory containing the subdirectories
parent_dir = '/home/ocanal/Escritorio/Trombosi'

# Initialize an empty list to store the data
all_data = []

# Iterate over the subdirectories
for subdir in os.listdir(parent_dir):
    
    subdir_path = os.path.join(parent_dir, subdir)
    if os.path.isdir(subdir_path):
        for file in os.listdir(subdir_path):
            
            if file.endswith("QC.xlsx"):
                file_path = os.path.join(subdir_path, file)
                df = pd.read_excel(file_path, engine="openpyxl")
                all_data.append(df)


        #create a joined_excels folder, if it haven't already exists

            output_directory = f"{parent_dir}/joined_excels"
            dir_exists = os.path.exists(output_directory)
            if dir_exists:
                pass 

            else:
                os.mkdir(output_directory)

# Concatenate all the data into a single DataFrame
all_data_df = pd.concat(all_data, ignore_index=True)

# Save the DataFrame to an Excel file
all_data_df.to_excel(f'{output_directory}/quality_control.xlsx', index=False)
