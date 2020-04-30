import re
fname = input("Enter file name: ")
fh = open(fname)
rg = []
tot = 0
for line in fh:
    line = line.rstrip()
    #print(line)
    
    k = re.findall('([0-9]+)',line) 
    #print(k)

    if k != [] :
        for m in range(0,len(k)) :
            i = int(k[m])
            rg.append(i)

#for num in rg :
#last = rg[len-1]
for n in range(0, len(rg)):
    tot = tot + int(rg[n])
print(tot)



    