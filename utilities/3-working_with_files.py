from pathlib import  Path
from time import  ctime
import shutil

# path=Path('abc.txt');

# print('Exists',path.exists())
# print('Rename',path.rename("jp_data.txt"))

path=Path("jp_data.txt");

print("Stats",path.stat())

print("Creation Time",ctime(path.stat().st_ctime))

# Reading the data from the file

data_from_file=path.read_text()
print(data_from_file)

# Old way of readin the file
print("-----old way-----------------")
with open("jp_data.txt","r") as file:
    data=file.read()
    print(data)

# --Write the data ------
path.open(mode="a")
path.write_text("this is some new somne data added")

#--Copy Paste------------

source=Path("jp_data.txt")
target=Path("abc.txt")

# target.write_text(source.read_text())

shutil.copy(source,target)