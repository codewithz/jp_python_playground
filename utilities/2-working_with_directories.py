from pathlib import  Path

path=Path('../ecommerce')

# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

print(path.iterdir())

for p in path.iterdir():
    print(p)

py_files=[p for p in path.glob("**/*.py")]
print(py_files)

directories=[p for p in path.iterdir() if p.is_dir()]
print(directories)