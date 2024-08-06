import ctypes

import os
import string




def read_files():
    res = []
    dir_path = r"D:\Scans\Freeman Archive\LTR009"
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    first_part: str = os.path.basename(res[0]).split("-")[0]
    for path in res:
        second_part: str = os.path.basename(path).split("-")[1]
        if first_part != os.path.basename(res[0]).split("-")[0]:
            print("Not all files have same folder number")
        else:
            new_name = "A0014-" +second_part
            new_full_name = os.path.join(dir_path,new_name)
            os.rename(os.path.join(dir_path,path),new_full_name)

    

out_count: int = 1

while(True):
    print("")
    print("Enter r to rename")
    in_var: str = input()
    if(in_var == "r"):
        read_files()
