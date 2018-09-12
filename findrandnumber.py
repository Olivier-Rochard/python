import random

n=random.randint(1,10)
g=0
while(g!=n):
    g=input('Quel est le nombre ?')
    g=int(g)
    if(g>n):
        print('trop grand')
    if(g<n):
        print('trop petit')
print('correct')
