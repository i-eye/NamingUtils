import ctypes
from operator import le
import os
import string




def read_files(count) -> bool:
    res = []
    dir_path = r"D:\Documents"
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)
    first_part: str = os.path.basename(res[0]).split("-")[0]
    for path in res:
        if first_part != os.path.basename(res[0]).split("-")[0]:
            print("Not all files have same folder number")
            return False
    if len(res) <= 26:
        letter_count = 97
        for path in res:
            if(count >= 10):
                new_name = first_part + "-"+str(count) + chr(letter_count) + ".jpg"
            else:
                new_name = first_part + "-0"+str(count) + chr(letter_count) + ".jpg"
            new_full_name = os.path.join(dir_path,new_name)
            os.rename(os.path.join(dir_path,path),new_full_name)
            letter_count += 1
        count += 1
    else:
        letter_count_one = 97
        letter_count_two = 97
        for path in res:
            if(count >= 10):
                new_name = first_part + "-"+str(count) + chr(letter_count_one) + chr(letter_count_two) + ".jpg"
            else:
                new_name = first_part + "-0"+str(count) + chr(letter_count_one) + chr(letter_count_two) + ".jpg"
            new_full_name = os.path.join(dir_path,new_name)
            os.rename(os.path.join(dir_path,path),new_full_name)
            letter_count_two += 1
            if (letter_count_two == (97 + 26)):
                letter_count_two = 97
                letter_count_one += 1
        count += 1
    return True

out_count: int = 1

while(True):
    print("")
    print("Enter r to rename, or s and a number(with space inbetween) to change the number")
    print("Enter c to get current count value")
    in_var: str = input()
    if(in_var == "r"):
        if read_files(out_count):
            out_count += 1
    elif(in_var.split()[0] == "s"):
        new_count = int(in_var.split()[1])
        if new_count > 0:
            out_count = new_count
            print("count is "+str(out_count))
        else:
            print("count of "+str(new_count)+ " is invalid, no change")
    elif(in_var == "c"):
        print("count is "+str(out_count))
    else:
        print("invalid input")