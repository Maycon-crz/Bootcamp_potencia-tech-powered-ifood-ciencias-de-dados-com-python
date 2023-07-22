while True:
    numero = int(input("Informe um numero: "))
    
    if(numero == 10):
        break
    
    print(numero)
    
    
for numero in range(100):
    # Exibe apenas os números impares
    if numero % 2 == 0:
        continue #É o contrário do break
    
    print(numero, end=" ")