import pandas as pd
from openpyxl import load_workbook

def edit_cell(file_path, sheet_name, col, row, new_value):
    print(f"Atualizando célula...jlmarangoni@netpage.com.br")
    # Abre o arquivo Excel
    workbook = load_workbook(filename=file_path)
    
    # Seleciona a planilha
    sheet = workbook[sheet_name]
    
    # Edita a célula
    sheet[f"{col}{row}"].value = new_value
    
    # Salva as alterações
    workbook.save(file_path)
    print(f"Célula {col}{row} foi atualizada para {new_value}")