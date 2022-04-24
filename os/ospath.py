import os


files_path = "files"



# C:\Users\facun\Desktop\programacion\python\python-practice
print(os.getcwd())

path_complete = os.path.join(os.getcwd(),files_path)

file_netflix= os.path.join(path_complete,"netflix_title.csv")