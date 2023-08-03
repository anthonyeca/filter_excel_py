import pandas as pd

def extract_different_rows(input_file_1, input_file_2, output_file):
    # Leer los archivos de Excel
    df1 = pd.read_excel(input_file_1)
    df2 = pd.read_excel(input_file_2)

    # Encontrar las filas que son diferentes entre ambos DataFrames en función de las columnas 'A' y 'B'
    different_rows_df1 = df1[~df1['A'].isin(df2['B'])]
    different_rows_df2 = df2[~df2['B'].isin(df1['A'])]
    
    # Concatenar los DataFrames resultantes para obtener el resultado final
    different_rows = pd.concat([different_rows_df1, different_rows_df2])
    
    # Guardar los resultados en un nuevo archivo de Excel
    with pd.ExcelWriter(output_file) as writer:
        different_rows.to_excel(writer, sheet_name='Filas_Diferentes', index=False)

# Ejemplo de uso
if __name__ == "__main__":
    input_file_1 = "archivo1.xlsx"  # Reemplaza con el nombre de tu primer archivo de entrada
    input_file_2 = "archivo2.xlsx"  # Reemplaza con el nombre de tu segundo archivo de entrada
    output_file = "filas_diferentes.xlsx"  # Reemplaza con el nombre del archivo de salida

    extract_different_rows(input_file_1, input_file_2, output_file)
