import itertools
arr = [1,2,3,4]
pailie = list(itertools.permutations(arr))
print(pailie)
for x in pailie:
    for y in x:
        print(y,end=' ')
    print()