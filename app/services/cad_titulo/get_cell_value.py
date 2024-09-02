import pandas as pd
from openpyxl import load_workbook

def get_cell_value(file_path, sheet_name, col, row):
    # Abre o arquivo Excel usando openpyxl
    workbook = load_workbook(filename=file_path, data_only=True)
    sheet = workbook[sheet_name]
    
    # Obtém o valor da célula diretamente usando col (ex: 'C') e row (ex: 5)
    cell_value = sheet[f"{col}{row}"].value
    
    return cell_value
