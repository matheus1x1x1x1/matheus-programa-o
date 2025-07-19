print('escolha uma operação')
print('1 - soma')
print('2 - subtração')
print('3 - multiplicação')
print('4 - divisão')

opção = input('digite o valor da operação desejada')
opção = int(opção)

num1 = int(input('digite o primeiro numero'))
num2 = int(input('digite o segundo numero'))

if opção == 1:
     resultado1 = num1 + num2
     print(f'a soma de {num1} + {num2} é {resultado1}')  

elif opção == 2:
     resultado2 = num1 - num2 
     print (f'a subtração de {num1} - {num2} é {resultado2}') 

elif opção == 3:
    resultado3 = num1 * num2 
    print(f'a multplicação de {num1} * {num2} é {resultado3}')

elif opção == 4:
     if num2 != 0 :
         resultado4 = num1 / num2
         print(f'a divisão de {num1} / {num2} é {resultado4}')
     else:
         print('erro: divisão por 0') 

else:
     print('opção invalida!')