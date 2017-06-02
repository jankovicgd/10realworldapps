import datetime

timenow = datetime.datetime.now()
timenowstr = timenow.strftime("%Y-%m-%d-%H-%M-%S-%f")

endfile = open(timenowstr + ".txt", 'a+')

filestomerge = ['file1.txt', 'file2.txt', 'file3.txt']

def filemerge(files):
    for file in files:
        currentfile = open(file, 'r')
        content = file.read()
        endfile.write(content)
        currentfile.close()
    endfile.close()

filemerge(filestomerge)
