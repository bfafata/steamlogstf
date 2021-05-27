import pathlib

myfile = pathlib.Path('myfile.txt')
pathlib.Path('')
myfile.touch(exist_ok=True)
f = open(myfile)