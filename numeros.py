Lista=[3,2,4,1,3,9]

for i in range(len(Lista)):
    for j in range(len(Lista)-i-1):
        if(Lista[j]> Lista[j+1]):
            Lista[j], [j+1], Lista[j]
print(Lista)