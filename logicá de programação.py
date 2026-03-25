import random
print('='*30)
print('EXERCICIO 01')
n1=int(input('Me de um nuemero: '))
n2=int(input('me de mais um numero: '))
print('A soma dos dois numero é {}'.format(n1+n2))
print('='*30)
print('EXERCICIO 02')
n1=int(input('Me de um numero: '))
impar=n1%2
if impar==0:
    print('O numero é par')
else:
    print('O nuemro é impar')
print('EXERCICIO 03')
n1=int(input('Me de um numero:'))
n2=int(input('Me de mais um numero:'))
n3=int(input('Me de mais um numero: '))
n4=int(input('Me só mais um numero:'))
if n1>n2 and n1>n3 and n1>n4:
    print('O maior numero é {}'.format(n1))
elif n2>n1 and n2>n3 and n2>n4:
    print('O maior numero pe {}'.format(n2))
elif n3>n1 and n3>n2 and n3>n4:
    print('O maior numero é {}'.format(n3))
else:
    print('O maior numero é {}'.format(n4))
print('='*30)
print('EXERCICE 04')
def exerciceo4():
   n1=float(input('Qual foi a sua primeria nota: '))
   n2=float(input('Qual foi a sua segunda nota : '))
   n3=float(input('Qual foi a sua terceira nota: '))
   media=(n1+n2+n3)/3
   print('Sua nota final foi {}'.format(media))
   return(media)
exerciceo4()
print('='*30)
print('EXERICE05')
media=exerciceo4()
if media <7:
    print('Você não passou')
else:
    print('Você passou!!!')
print('='*30)
print('EXERCICIO06')
idade=int(input('Quantos anos você tem?'))
if idade <18:
    print('você é menor de idade')
elif idade >=18 and idade <= 59:
    print('Você é um adulto')
else:
    print('Você é um idoso:')
print('='*30)
print('EXERCICE07')
n1=int(input('Me de um numero:  '))
n2=int(input('Me de um numero:'))
print('A soma dois numeros dá {}\n A divisão dos numeros resultam em {}\n A multiplicação dos numero dá {}\n A subtração dos numero dã {}'.format(n1+n2, n1/n2, n1*n2, n1-n2)) 
print('='*30)
print('EXERCICE 08')
def exerciceo4():
   n1=float(input('Qual foi a sua primeria nota: '))
   n2=float(input('Qual foi a sua segunda nota : '))
   n3=float(input('Qual foi a sua terceira nota: '))
   media=(n1+n2+n3)/3
   print('Sua nota final foi {}'.format(media))
   return(media)
exerciceo4()
print('='*30)
print('EXERICE09')
exerciceo4()
if media <7:
    print('Você não passou')
else:
    print('Você passou!!!')
print('='*30)
print('EXERCICIO010')
for i in range(0, 11):
    print(i)
print('='*30)
print('EXERCICE011')
n1=int(input('Me de um numero'))
n2=int(input('Me de um numero:'))
n3=int(input('Me de mais um numero: '))
n4=int(input('Me de mais um numero: '))
n5=int(input('Me de só mais um numero: '))
somat=n1+n2+n3+n4+n5
print('A soma dos numeros resultam em {}'.format(somat))
print('='*30)
print('EXERCICIO012')
n1=int(input('Me de um numero: '))
for i in range(0, 11):
    print('{}x{}={}'.format(n1, i, n1*i))
print('='*30)
print('EXERCICIO013')
aleatirio=random.randint(0, 10)
tentar=""
while tentar!=aleatirio:
    tentar=int(input('Em qual numnero eu tó pensando?'))
    if tentar==aleatirio:
        print('Você acertou !!')
    elif tentar>aleatirio:
        print('Você errou por {} a menos'.format(tentar-aleatirio))
    else:
        print('Você errou por {} a mais '.format(aleatirio-tentar))
print('='*30)
print('EXERCICIO014')
nome_de_usuario=str(input('Qual o nome do seu perfil? '))
senha_de_usuario=int(input('Qual vai ser a senha? '))
nome_tenta=""
senha_tenta=""
while nome_de_usuario!=nome_tenta and senha_de_usuario!=senha_tenta:
    nome_tenta=str(input('Qual é o nome da conta? '))
    senha_tenta=int(input('Qual é a senha da conta? '))
    if nome_tenta==nome_de_usuario and senha_tenta==senha_de_usuario:
        print('Olá de novo {}'.format(nome_de_usuario))
    elif nome_tenta!=nome_de_usuario and senha_tenta!=senha_de_usuario:
        print('As credencias estão incorretas')
    elif nome_tenta!=nome_de_usuario and senha_tenta==senha_de_usuario:
        print('As credencias estão incorretas')
    else:
        print('As credencias estão incorretas')
print('='*30)
print('EXERCICIO015')
saldo=1000
menu=str(input('Olá oque vc gostaria de fazer hj? n\ 1.sacar 2.depositar 3.ver saldo'))
if menu=='sacar':
    menos=int(input('Quantos R$ você quer sacar?'))
    print('R$-{}'.format(saldo-menos))
    print('Você tem R${}na conta agora '.format(menos-saldo))
elif menu=='depositar':
    mais=int(input('QUantos você vai depositar? R$'))
    print('R$+{}'.format(saldo+mais))
    print('Agora você tem na conta R${}'.format(saldo+mais))
else:
    print('Você tem na conta R${}'.format(saldo))
