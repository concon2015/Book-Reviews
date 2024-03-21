cubes = [value**3 for value in range(1,11)]
for cube in cubes:
    print(cube)

print(f'The first three items in the list are {cubes[:3]}')
print(f'The middle three items in the list are {cubes[4:7]}')
print(f'The last three items in the list are {cubes[7:]}')