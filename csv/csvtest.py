import csv
import os


print(os.path.join(os.getcwd(),'csv','netflixfile.csv'))

path= os.path.join(os.getcwd(),'csv','netflix_titles.csv')
file = open(path,"r",encoding='utf-8')

csvreader = csv.reader(file,delimiter=',')

# header = next(csvreader)
# print(header)
# header = next(cvsreader)
# print(header)

for linea in csvreader:
  if linea[1] == "TV Show" and linea[5] == "Argentina":
    # la linea es una lista
    # print(type(linea))
    print(f"{linea[2]:<40} {linea[3]}")

# file.close()


# restart file read position
file.seek(0)

# otra forma de lerlo con lambdas y filter

shows_ar = filter(lambda x: x[5] == "Argentina" and x[1] == "TV Show",csvreader)
for elem in shows_ar:
  print(f"{elem[2]:<40} {elem[3]}")
print(shows_ar)

file.seek(0)


#  reading with DictReader to get the information on objects/dics
csvDict=csv.DictReader(file,delimiter=',')

print(csvDict.fieldnames)
print(csvDict.dialect)
print(csvDict.line_num)
print(csvDict.reader)
print(csvDict.restkey)
print(csvDict)

# for line in csvDict:
#     print(line)



file.close()