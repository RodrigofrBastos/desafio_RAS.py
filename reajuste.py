"""
Rodrigo Freire Bastos
Criar um programa onde o usuário deverá selecionar o reajuste e logo em seguida digitar o salário. O sistema deve calcular o valor do reajuste
"""

import time 


print('\n\nOla usuario, esta plataforma ira informa-lo o valor do seu salario com o reajuste escolhido por voce! \n\n\n')
time.sleep(4)


print('1 -> Reajuste de 3,43%')
print('2 -> Reajuste de 6,58%')
print('3 -> Reajuste de 11,28% \n\n')


reajuste = int(input('Agora, me diga qual dos reajustes acima voce deseja escolher: '))

salario = int(input('Para finalizar, me informe seu salario: '))

if(reajuste == 1):
    novoSalario = salario * 1.0343
    
    print('\n\nSalario reajustado: R$', round(novoSalario, 2))

elif(reajuste == 2):
    novoSalario = salario * 1.0658
    
    print('\n\nSalario reajustado: R$', round(novoSalario, 2))

elif(reajuste == 3):
    novoSalario = salario * 1.1128
    
    print('\n\nSalario reajustado: R$', round(novoSalario, 2))

else:
    for i in range(3):

        print('\n1 -> Reajuste de 3,43%')
        print('2 -> Reajuste de 6,58%')
        print('3 -> Reajuste de 11,28% \n\n')

        Reaj = int(input('Valor invalido, digite novamente: '))

        if(Reaj == 1):
            novoSalario = salario * 1.0343
            
            print('\n\nSalario reajustado: R$', round(novoSalario, 2))
            break

        elif(Reaj == 2):
            novoSalario = salario * 1.0658
            
            print('\n\nSalario reajustado: R$', round(novoSalario, 2))
            break

        elif(Reaj == 3):
            novoSalario = salario * 1.1128
            
            print('\n\nSalario reajustado: R$', round(novoSalario, 2))
            break
        
        else:
            continue



