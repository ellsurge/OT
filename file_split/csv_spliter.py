import csv
from math import ceil
import os

# change to the file

filename = "hrl2tosplit"
batch = 200
parts =  ['split'] #if you want yo eg, ['DAVID', 'JOHN', 'CHAT'] or [1,2]


def mk(dir):
    out = 0
    try:
        os.mkdir('splits/'+part_path)
        out =1
        
    except OSError as error:
        out = (0,error)
    return out


print('loading file...')
file = open(filename+".csv")
count= 1
nof =1
write =''
f = ''

print('writing splits...')

csvr = csv.reader(file)
part_no = 0
part_size = ceil((sum(1 for row in csvr)/batch)/len(parts))

part_path = 'splits/'+parts[part_no]
for row in csvr:
    
    if not nof % part_size :
        part_no += 1
        m=  mk('splits/'+part_path)
        if m[0]:
            part_path = 'splits/'+parts[part_no]
        else:
            print(m[1])
            part_path = 'splits/'            

        try:
            print('#####errorr')
            print(nof)
            os.mkdir('splits/'+part_path)
            part_path = 'splits/'+parts[part_no]
            
        except OSError as error:
            print(error)
            part_path = 'splits/'
    if(count ==1):
        f= open('{}/split{}.csv'.format(part_path, str(nof)), 'w')
    if(count == batch):
        write = csv.writer(f)
        write.writerow(row)
        count =1
        nof +=1
        f.close()
    else:
        write = csv.writer(f)
        write.writerow(row)
        


        count +=1
    
