name = 'Connor'
numbers = list(range(1,21,2))
print('Is name == "Jeffrey"? I predict False')
print(name=='Jeffrey')

print('Is name == "Jeff"? I predict False')
print(name=='Jeff')

print('Is name == "Conor"? I predict False')
print(name=='Conor')

print('Is name == "Coonor"? I predict False')
print(name=='Coonor')

print('Is name[0] == "c"? I predict False')
print(name[0]=='c')

print('Is name == "Connor"? I predict True')
print(name=='Connor')

print('Is name[0]=="C"? I predict True')
print(name[0]=='C')

print('Is name[0:3]=="Con"? I predict True')
print(name[0:3]=='Con')

print('Is name[3:5]=="nor"? I predict True')
print(name[3:6]=='nor')

print('Is name == "Connor"? I predict True')
print(name.lower()=='connor')

print("Is 2 in numbers? I predict False")
print(2 in numbers)

print("Is 2 not in numbers? I predict True")
print(2 not in numbers)

print("Is 2 > 4? I predict False")
print(2 > 4)

print(True and True)

print(True or False)
