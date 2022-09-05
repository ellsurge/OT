import pandas as pd
import numpy as np


##edit start--- here
no_of_splits = 10
file_name = 'NHF_CONTRIBUTION_UPLD.xlsx'
file_dir = '.'
output_folder ='EXCEL_SPLITS'
split_name = file_name+'_split'

##edit end--- here


print("loading file...")
i =1
df = pd.read_excel(file_name)
fs = len(df)
chunksize = int(fs/no_of_splits)
def offset(x):
    return x-1
print('spliting file...')
def cs(chunksize, fs):
    sa = []
    num =chunksize
    while(num< fs):
        sa.append(num)
        num += chunksize
    sa.append(num+fs%chunksize)
    return sa


for chunk in np.split(df, cs(chunksize,fs)):
    chunk.to_excel('{}/{}_{:02d}.xlsx'.format(output_folder,split_name, i), index=False)
    i +=1
print('Done.')