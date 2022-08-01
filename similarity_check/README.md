# Similarity check 
this runs a simirity check on two exect collums from wither same file
***

## SETUP
***
asiuming you have python already installed
if not get it at [python offical page](https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe)

to get started after a proper installation of python, you'd need the following tools

* numpy
* pandas
* fuzzywuzzy
* os  

to install the folloing, use `pip` to install 

`pip install numpy`

`pip install pandas`

`pip install fuzzywuzzy`

`pip install os`  _optional_

---
## USAGE
---
## step1: entering imput parameter
these can be found at line 11 of the code

    `11 #---------------------EDIT  START HERE-------------------------`

- `file_path`: if the file is in the same dir as the python file, do not change this

- `file_name`: change this to the name if the excel file, without any extentions

- `name1_coll_name`: change this to the name of the first column

- `name2_coll_name`: change this to the name of the second column 

- `output_path` (optional) : similar to the file path, the output path where the output is to be , on default is creates a file with the sanem name as the input file

- `output_name` (optional) : similar to the file name, its the name of the output file , on default is creates a file with the same name as the input file

## step2: running the code

to run the code, first open your terminal and make sure you are in the file as the similarity check, 

on windows use `cd` 

then type this following line

`python name_similarity_checker.py`

or if youre using python3 

`python3 name_similarity_checker.py`

---
## OUTPUT FORMAT
the output on deafut out be formarted in this format

FILENAME_CORRECT

FILENAME_MAYBE

FILENAME_WRONG 

these three levels are the accuracy levels of the comparison
