filepath = 'elink-mapping-11-02-2020.tab'

file=open(filepath)
data=file.readlines()

#counts the lines in file and prints
linecount=0
for i in data:
    if i:
        linecount += 1
print("# of lines in: ", filepath)
print(linecount,"\n")

#just test printing variables
#print(file)
#print(data[2])

#try to print full data prettier
#for line in data:
#    print(line, \"\\n\")

#strip removes white space from beginning and end of data, maybe not necessary?
linesplit=data[1].strip().split('|')
#taking variables from split.  0 is always blank, 1 is location and type, 2 is inner wagon, 3 is outer wagon
[endcap, layer, cassette, mbIndex, mbType, organization, approxpos] = linesplit[1].split(',')
innerwagon = linesplit[2]
outerwagon = linesplit[3]


#print(linesplit)
#print(data[1])
print(linesplit[1])
print(endcap)
print(innerwagon)
 