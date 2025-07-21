from pathlib import Path

Path(r"c:\Users\oyinl\PythonTutorials\CodeWithMosh")
Path()
Path.home()

path = Path(r"c:\Users\oyinl\PythonTutorials\CodeWithMosh")
path.exists()
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path.absolute())
