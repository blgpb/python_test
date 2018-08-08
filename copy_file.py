filename = input('Please input the filename that want to be copyed:')
old_file = open(filename, 'r')
new_file = open(filename+'_copy', 'w')

while True:
    content = old_file.read(1024)
    if len(content) == 0:
        break
    new_file.write(content)

old_file.close()
new_file.close()