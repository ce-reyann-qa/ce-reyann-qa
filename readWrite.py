file = open('test.txt')
#Read all the contents of file
#Read a number of characters by using parameter

#print(file.read(5))

#print(file.readline())
#print(file.readline())
#file.close()


#print line by line using readline method
#line = file.readline()
#while line != "":
   # print(line)
   # line = file.readline()


#values = [cat, dog, spider, bear, wolf]
for line in file.readlines():
    print(line)


file.close()