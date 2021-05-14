import pathlib

myfile = pathlib.Path('myfile.txt')
myfile.touch(exist_ok=True)
f = open(myfile)