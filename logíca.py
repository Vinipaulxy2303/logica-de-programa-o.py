print('\033[33m-='*30)
print('\033[7;34mOlá mundo\033[m ')
print('\033[33m-=\033[m'*30)
nome=input('Qual seu nome?')
print('Olá {}, seja be, vindo!!!'.format(nome))
n1=int(input('Me de um numero!'))
n2=int(input('Me de outro numero:'))
print('os possiveis resultados das contas são :')
print('\nsoma {}\nsubtração {}\nmultiplicação {}\ndivisão {}\n elevado {} e {}\n'.format(n1+n2, n1-n2, n1*n2, n1/n2, n1^2, n2^2))
peso=float(input('Qual seu peso: '))
altura=float(input('Qual a sua altura: '))
imc=peso/(altura**2)
print(imc)
if imc >= 18.5 or imc <= 25:
    print('Seu peso está no ideal para sua altura: ')
else:
    print('Seu peso não está na altura ideal: ')
if imc < 17.0:
    print('Você está muito magro')
elif imc == 17.0 or imc == 18.5:
    print('Você está abaixo do peso')
elif imc > 18.5 or imc == 25:
    print('Você está no peso ideal')
elif imc> 25 or imc == 30:
    print('Você está com sobrepeso')
elif imc> 30 or imc == 35:
    print('Você está obeso')
elif imc> 35 or imc >= 40:
    print('Você está obesidade severa')
else:
    print('Você está com obesidade morbida')
print('\033[33m-='*30)
print('DEPERTAMENTO DE TRANSITO')
print('\033[33m-='*30)
anoatual=int(input('ANO ATUAL (yyyy): '))
ano_de_nascimento=int(input('ANO DE NASCIMENTO (yyyy): '))
idade=anoatual-ano_de_nascimento
print('\033[33m-='*30,'STATUS','\033[33m-='*30)
if idade >= 17:
    print('Você pode ter uma carteira de motorista')
else:
    print('Você não pode ter carteira de motorista')
print('\033[33m-='*60, '\033[m')
contador=int(input('Me de um numero :'))
for i in range(contador) :
    print(i +1)

