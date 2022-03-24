from pathlib import  Path

path1=Path("D:\\Zartab\\Trainings")
print(path1)
# path2=Path('/usr/local/bin') Linux and Mac

currentPath=Path()
print(currentPath)

path3=Path("../ecommerce/__init__.py")
print(path3)

combinedPath=Path() / Path('test')

print(combinedPath)

print("Exists",path3.exists())
print("Is File",path3.is_file())
print("Is Dir",path3.is_dir())

print(path3.name)
print(path3.stem)
print(path3.suffix)
print(path3.parent)
print(path3.absolute())
newFilePath=path3.with_name("newFile.txt")
print(newFilePath)