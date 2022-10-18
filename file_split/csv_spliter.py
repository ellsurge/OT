import csv
from math import ceil
import os
import string

# change to the file

filename = "new"
batch = 5
parts =  ['call','james'] #if you want yo eg, ['DAVID', 'JOHN', 'CHAT'] or [1,2]
dev_mode = False


#---------------------------* do not touch *---------------------------------------------






def mk(dir):
    out = 0
    try:
        os.mkdir(dir)
        out =[1]
        
    except OSError as error:
        out = [0,error]
    return out
def log(*args):
    if dev_mode:
    
        st= ""
        for s in args:
            st +=str(s)+" "
        print(st)
        

print('loading file...')
file = open(filename+".csv")
count= 0
nof =0
write =''
f = ''

print('writing splits...')

csvr = csv.reader(file)

part_no = 0
part_size = ceil((sum(1 for row in csvr)/batch)/len(parts))
file = open(filename+".csv")
csvr = csv.reader(file)


mk('splits')
lock = True      
for row in csvr:
    log('row:',count)
    if not bool(nof % part_size) and part_no < len(parts) and lock :
        log('################## ',nof,' nod', part_size)
        m=  mk('splits/'+parts[part_no])
        if bool(m[0]):
            part_path = 'splits/'+parts[part_no]
        else:
            log(m[1])
            part_path = 'splits/'            
        part_no +=1
        lock = False
    if(count ==0):
        log("--------opeing a new file")
        f= open('{}/split{}.csv'.format(part_path, str(nof)), 'w')
        
    if(count == batch):
        log('--------write done:',count)
        
        write = csv.writer(f)
        write.writerow(row)
        
        count =0
        nof +=1
        f.close()
        lock = True
    else:
        log('writing line:',count)
        write = csv.writer(f)
        write.writerow(row)
        count +=1
print("done")
