import re
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    #print(line)
    #try:
    lst = re.findall('\s([0-9]+)',line)
    #except:
        #continue
print(lst)