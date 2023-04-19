import sys
import qrcode
import os

def approve():
    x = input ("Are you sure?? [y/n]\n")
    x = x.lower()
    return x

if len(sys.argv) > 2:
    data = sys.argv[1]
    file_name = sys.argv[2]
    img = qrcode.make(data)
    if os.path.exists(file_name):
        print(f"the file '{file_name}' will be overwritten!")
        x = approve()
        if x == "y" or x == "yes":
            img.save(file_name)
        elif x == "n" or x == "no":
            print("operation aborted")
        else:
            print("please answer with [y/n]!")
            print("operation aborted")
    else:
        img.save(file_name)
else:
    print('Usage: write.py "{data}" {file name}')
