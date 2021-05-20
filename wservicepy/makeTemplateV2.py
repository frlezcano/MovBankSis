import re
from datetime import date
import pandas as pd
from pandas import ExcelWriter

#Día actual
today = date.today()
formatedToday = today.strftime('%m/%d/%Y')

### datetimestring = 
### datetimestring = re.sub('[-.:]', '/', datetimestring)

### formatedToday = datetime.strptime(today, '%m/%d/%y')

'''
    INTO stdmvcta(cod_banco, cod_ctacte, fec_ope, fec_recaud, doc_ref,
      cod_ope, tip_pag, monto_gs, estado, glosa, tip_mov_ba, cod_error,
      nro_mov)
    VALUES(cod_banco, cod_ctacte, fec_ope, fec_recaud, doc_ref, cod_ope,
    'O',
    monto_gs,
    'N',
    glosa, tip_mov_ba,
    NULL,
    NULL)
'''


df = pd.DataFrame({'cod_banco': [7],
                   'cod_ctacte': [6001007123],
                   'fec_ope': [formatedToday],
                   'fec_recaud': [formatedToday],
                   'doc_ref': [1],
                   'cod_ope': [1],
                   'tip_pag': ['O'],
                   'monto_gs': [1],
                   'estado': ['N'],
                   'glosa': [1],
                   'tip_mov_ba': [1],
                   'cod_error': ['NULL'],
                   'nro_mov': ['NULL']})
df = df[['cod_banco', 'cod_ctacte', 'fec_ope', 'fec_recaud', 'doc_ref', 'cod_ope', 'tip_pag', 'monto_gs', 'estado', 'glosa', 'tip_mov_ba', 'cod_error', 'nro_mov']]
writer = ExcelWriter('/home/rlezcano/tmp/wservicepy/Plantilla_Banco7_Cta6001007123.xlsx',date_format='mm/dd/yyyy')
df.to_excel(writer, 'Movimientos Bancarios', index=False)

formatdict = {'num_format':'mm/dd/yyyy'}
fmt = workbook.add_format(formatdict)

worksheet.set_column('A:A', None, fmt)

writer.save()


'''
df = pd.DataFrame({'Id': [1, 3, 2, 4],
                   'Nombre': ['Juan', 'Eva', 'María', 'Pablo'],
                   'Apellido': ['Méndez', 'López', 'Tito', 'Hernández']})
df = df[['Id', 'Nombre', 'Apellido']]
writer = ExcelWriter('/home/rlezcano/tmp/wservicepy/ejemplo.xlsx')
df.to_excel(writer, 'Hoja de datos', index=False)
writer.save()
'''