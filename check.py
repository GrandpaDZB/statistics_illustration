import os

check_page = input("check page: ")
folder_list = os.listdir()
if "p"+check_page in folder_list:
    print("Existed.")
else:
    print("Not found.")