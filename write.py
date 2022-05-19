with open('test.txt', 'r') as reader: #readmore r
    content = reader.readlines() #from first to last
    reversed(content) #from last to first
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)
