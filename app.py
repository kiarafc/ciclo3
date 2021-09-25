numero = int(input('Digite el nuermo a verificar: '))

cont=0
for i in range (1, numero +1):
    if numero%i==0:
        cont = cont+1
if cont ==2:
    print('El numero es primo')
else:
    print('El numero no es primo')

