from mysqlx import Column
import pandas as pd
files = [
    'employee 1405',
    'employee'
]
output=  'sms'
file_extention = '.xlsx'


final =pd.read_excel(files[0]+'.xlsx')
c =0
for file in files:
    if(c !=0):
        f = pd.read_excel(file+file_extention)
        final = pd.concat([final, f])
    c += 1
final.to_excel('merge/'+output+'_MERGE'+file_extention, index ='false')
