from datetime import date
import pandas as pd
from pandas import ExcelWriter
#import xlsxwriter

#Día actual
today = date.today()
#formatedToday = today.strftime('%m/%d/%Y')

#Libro de Excel
filePath  = '/home/rlezcano/tmp/wservicepy/'
filename  = 'Plantilla_Banco7_Cta6001007123.xlsx'

#Crea datos de ejemplo
dataframe = pd.DataFrame({'cod_banco': [7],
                   'cod_ctacte': [6001007123],
                   'fec_ope': [today],
                   'fec_recaud': [today],
                   'doc_ref': [1],
                   'cod_ope': [1],
                   'tip_pag': ['O'],
                   'monto_gs': [1],
                   'estado': ['N'],
                   'glosa': [1],
                   'tip_mov_ba': [1],
                   'cod_error': ['NULL'],
                   'nro_mov': ['NULL']})

#Crea Título de Columnas
#dataframe = dataframe[['cod_banco', 'cod_ctacte', 'fec_ope', 'fec_recaud', 'doc_ref', 'cod_ope', 'tip_pag', 'monto_gs', 'estado', 'glosa', 'tip_mov_ba', 'cod_error', 'nro_mov']]

#dataframe['fec_ope2']=pd.to_datetime(formatedToday)


writer = pd.ExcelWriter((filePath + filename), engine='xlsxwriter', date_format='dd/mm/yyyy')



# Convert the dataframe to an XlsxWriter Excel object.
dataframe.to_excel(writer, sheet_name='Movimientos Bancarios', index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook  = writer.book
worksheet = writer.sheets['Movimientos Bancarios']

# Formato a columnas de tipo fecha
# worksheet.write_datetime(1, 2, today)
# worksheet.write_datetime(1, 3, today)

# Formato de cabecera
# Add a header format.
header_format = workbook.add_format({
    'bold': True,
    'text_wrap': True,
    'valign': 'top',
    'fg_color': '#d3e2b6',
    'border': 1})
for col_num, value in enumerate(dataframe.columns.values):
    worksheet.write(0, col_num, value, header_format)

# Formato para columnas de tipo fecha
formatdict = {'num_format':'mm/dd/yyyy'}
fmt = workbook.add_format(formatdict)
worksheet.set_column('C:C', None, fmt)

# Ajuste de ancho de columnas para mejor lectura
worksheet.set_column('A:D', 15)
worksheet.set_column('E:M', 10)

# Escritura del archivo excel
writer.save()

