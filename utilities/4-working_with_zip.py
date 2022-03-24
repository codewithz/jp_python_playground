from pathlib import  Path
from zipfile import  ZipFile

# zip=ZipFile("files.zip","w")

# #Writing to zip
#
# for path in Path('../ecommerce').rglob("*.*"):
#     zip.write(path)
#
# zip.close()

#Extract from a Zip
with ZipFile('files.zip') as zip:
    print(zip.namelist())
    zip.extractall("myfiles")