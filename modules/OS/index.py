import os

#print("My current location: "+os.getcwd()) #Current path

folder_name = "demoFolder"
if not os.mkdir().exists(folder_name):
    create_folder = os.mkdir(folder_name)
    print(f"{create_folder} {folder_name} has been created")
else:
    print(f"{folder_name} all ready exists")
