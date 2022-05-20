from numpy import average
import pandas as pd
from fuzzywuzzy import fuzz
import os 





#---------------------EDIT  START HERE-------------------------
#INPUT 
filepath = '.'      #where file is located
filename = 'PassedSimilarityCheck'     #name of the file 
# name2_coll_name = 'NIBSSName'   #first column 
name2_coll_name = 'DBName'         #first column 
name1_coll_name = 'BENEFICIARY'         #first column

#OUTPUT
output_path = filename#'new_test_RESULTS'
output_name = filename
#---------------------EDIT ENDS HERE---------------------------




#CODE 
titles =['MRS.', 'MS.', 'MR.', 'MISS.','MRS', 'MS', 'MR', 'MISS']
illegals =('.',',','_','-','?','�','null', '|', '@', '')
demacators = '-'

nicks= ['MOHD', 'MUHD', "MUH'D"]
fulls = ['MOHAMMED', 'MUHAMMAD','MUHAMMAD']

print('-----------------------------\nloading data..')
data = pd.read_excel("{}/{}.xlsx".format(filepath, filename))
colls = pd.Series(data.axes[1]).values

correct = pd.DataFrame(columns=colls)
maybe = pd.DataFrame(columns=colls)
wrong = pd.DataFrame(columns=colls)


def remove_dot(s):
    for i in demacators:
        s =s.replace(i, ' ')
    for i in illegals:
                                                                                                        # print('\n\n-------------------------------------\n',i)
                                                                                                        # print('\n-------------------------------------\n',)
        s = s.replace(i, '')
    return s
def compare(name1, name2):
    count = 0
    for name in name1:
        if name.upper() in nicks:
                                                                                                        # print('\n\n-------------------------------------\n',name)
            name = fulls[nicks.index(name.upper())]
                                                                                                        # print(name,'\n-------------------------------------\n\n')

        nc = 0
        initial_cache = []
        if name.upper() in titles :
            count +=1
                                                                                                        # print('here title' )
        else:   
            for n in name2:
                if n.upper() in nicks:
                                                                                                        # print('\n\n-------------------------------------\n',n)
                    n = fulls[nicks.index(n.upper())]
                                                                                                        # print(n,'\n-------------------------------------\n\n')
                else:
                    if len(name) >2 :
                        if(name.upper() in n.upper() or fuzz.ratio(name.upper(), n.upper()) >= 75):
                            count += 1
                        elif (name[0].upper() == n):
                            count += .5
                                                                                                        # print('here match', name, n)

                    else:
                        if((name[0].upper() in n.upper()) and (name not in initial_cache)):
                            count +=1 
                                                                                                        # print('here initial' )

                            initial_cache.append(name)
    return count
        






print('-----------------------------\ncomparing names..')
for index, row in data.iterrows():

    name1 = list(map(remove_dot, str(row[name1_coll_name]).split()))
    name2 = list(map(remove_dot, str(row[name2_coll_name]).split()))
    while "" in name1:
        name1.remove("")

    while "" in name2:
        name2.remove("")   
    d_row = pd.DataFrame([row.values],columns=colls)

    count1 = compare(name1, name2)
    count2 =  compare(name2, name1)

    agg_count = average([count1, count2])

    len1 = len(name1)
    len2 = len(name2)
    agg_len = average([len1, len2])


    ratio = (agg_count/agg_len)

    if ratio >= 0.75:
        correct = pd.concat([correct,d_row], ignore_index=True)

    elif 0.45< ratio <0.75:
        maybe = pd.concat([maybe,d_row], ignore_index=True)

    else:
        wrong = pd.concat([wrong,d_row], ignore_index=True)





try: 
    print('-----------------------------\ncreating dir')
    os.mkdir(output_path)
except OSError as error:
    print(error)
finally:
    print('dir created')
print('-----------------------------\nwriting to file..')
correct.to_excel('{}/{}_CORRECT.xlsx'.format(output_path, output_name), index =False)
maybe.to_excel('{}/{}_MAYBE.xlsx'.format(output_path, output_name), index =False)
wrong.to_excel('{}/{}_WRONG.xlsx'.format(output_path, output_name), index =False)
print('-----------------------------\nDone')



