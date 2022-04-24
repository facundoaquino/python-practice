

from asyncore import write
import csv
from importlib.resources import path
import os


file_path = os.path.join(os.getcwd(),'csv','bands.csv')
print(file_path)

file=open(file_path,'w',encoding='utf-8')
csvwriter =csv.writer(file)

csvwriter.writerow(["name","city","ref"])