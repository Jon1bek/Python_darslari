with open( 'jonibek.txt') as file:
    J = file.read()
print(J)
J = J.rstrip()
J = J.replace('\n','')
print(J)