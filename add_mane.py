import csv
import pandas as pd

mane_file = "/home/ocanal/vep_data/mane_data/MANE.GRCh38.v1.0.summary.txt"

def extract_excel_column(excel_path, sheet_name, column_name):
    df = pd.read_excel(excel_path, sheet_name=sheet_name)
    column_values = df[column_name].tolist()
    return column_values


def parse_mane_txt(mane_file, feature_list):

    
    with open(mane_file, "r") as mane_f:
        reader = csv.reader(mane_f, delimiter ="\t")
        column_values = [row["MANE_status"] for row in reader]

    mane = []
    for feature in feature_list:
        if feature in column_values:
            mane.append(value)
        else:
            mane.append("-")

    return mane

def extract_column_from_tab_file(tab_file, feature_list_to_compare, feture_to_extract):
    with open(tab_file) as tab_f:
        reader = csv.reader(tab_f, delimiter = "\t")
        column_values = [row[column] for row in reader]

    output_columns = []

    for feature in feature_list_to_compare:
        if feature in column_values:
            output_columns.append(value)
        else:
            return "error"

uploaded_variations = extract_excel_column("/home/ocanal/Escritorio/Trombosi/joined_excels/variants_joined.xlsx", "Sheet1", "Uploaded_variation")

print (uploaded_variations)

def merge_pandas():
    df1 = pd.read_csv(mane_file, delimiter ="\t")

    df2 = pd.read_excel("/home/ocanal/Escritorio/Trombosi/joined_excels/variants_joined.xlsx", sheet_name="Sheet1")
    merged_df = pd.merge(df1,df2, on="Uploaded_variation")
    print(merged_df)

merge_pandas()