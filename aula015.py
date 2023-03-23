nome = input('Qual o seu nome? ')

numero_1 = input('Digite sua idade: ')
numero_2 = input('Digite os anos que falta para o termino da sua faculdade: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'Meu nome é {nome}, tenho {numero_1} anos e vou ter {int_numero_1 + int_numero_2} anos quando terminar minha faculdade.')
