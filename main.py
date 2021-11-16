# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import zipfile

print('''
#########  #########  ######### ########## #       # ######### ############ #########
#       #  #       #  #       #    ###     #       # #       #     ###      #        
#########  #       #  #       #    ###     ######### #########     ###      #########
#       #  #       #  #       #    ###     #       # #       #     ###              #
#       #  #########  #########    ###     #       # #       #     ###      ######### 
''')

count = 1

passwordlist = input("Enter Your Passwordlist NamePath :")
zipfile_name = input("Enter Your ZipFile NamePath :")

with open (passwordlist,'rb') as pwd:
    for entry in pwd.readlines():
        password = entry.strip()

        try:
            with zipfile.ZipFile(zipfile_name,'r') as zf:
                zf.extractall(pwd=password)
                print(f"********** Password Found = {password.decode('utf8')} **********")
                break

        except:
            number = count
            print(f"{number} Password Faild = {password.decode('utf8')}")
            count +=1
            pass


