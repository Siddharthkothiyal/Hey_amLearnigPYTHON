# f=open('file.txt')
# data= f.read()
# print(data)
# f.close()

# str= "I am fine what about you?"
# f=open('file.txt', 'w')
# f.write(str)
# f.close()


# to read Multiple lines
f= open('file.txt')
lines = f.readlines()
print(lines , type(lines))