import random

secret=int(random.randrange(1,10))
n=0
while n!=secret:
    while n<1 or n>10:
        n=int(input("Digite un numero entre 1 y 10: "))
        if n<1 or n>10:
            print("Digite un numero valido. (entre 1 y 10)")
            n=0
        elif n!=secret:
            print("¡Ja, ja! ¡Estas atrapado en mi bucle!")
            n=0
print("¡Bien hecho muggle! Eres libre ahora.")