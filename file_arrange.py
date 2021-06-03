#import all libraries
import os
import re
import tkinter
from tkinter import filedialog

#get the userpath 
root = tkinter.Tk()
root.withdraw()

ch=''
while ch!='y':
    user_path = filedialog.askdirectory()
    ch=input("y/n?")

os.chdir(user_path)
files=os.listdir(user_path) #list of all files

ext_arr=[]
ext_arr_final=[]
extension_set={}
folder_names=[]
folder_names_final=[]

#get the extension of all files
regex_ext="\.{1}[a-zA-Z34]*$"
for items in files:
    ext_match = re.compile(regex_ext)
    ext_arr.append((ext_match.findall(items)))
for ext in ext_arr:
    for e in ext:
        ext_arr_final.append(e)
extension_set=set(ext_arr_final)  #set of extension

#get the folder name with the name of extensions
regex_folder="[a-zA-Z34]*$"
for item in extension_set:
    fold_match=re.compile(regex_folder)
    folder_names.append((fold_match.findall(item)))

for name in folder_names:
    for items in name:
        if len(items)>0:
            folder_names_final.append(items)

#create folders 
for name in folder_names_final:
    if(os.path.exists(name))==0:
        os.mkdir(name)
        
#get files and chnage directory followed its respective folder 
for items in files:
    file_match=re.compile(regex_ext)
    file_extension=(file_match.findall(items))
    for item in file_extension:
        if item in extension_set:
            get_folder_name=fold_match.findall(item)
            for name in get_folder_name:
                if len(name)>0:
                    get_folder_name=name
            os.rename(f"{items}",f"{user_path}/{get_folder_name}/{items}")
print('Done')
