#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words 
#using the split() method. The program should build a list of words. For each word on each line check to see
#if the word is already in the list and if not append it to the list. When the program completes, sort and 
#print the resulting words in alphabetical order. 

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    k = line.split()
    print(k)
    #print(len(k))


    #for i in range(k)
    for i in k:
        #print(i)
        if not i in lst: 
            lst.append(i)
    #continue
    #print(lst)
lst.sort()
print(lst)
#print(len(lst))
#print(k)
#print(line.rstrip())

