import datetime
agora = datetime.datetime.now() #horas 
hora = agora.hour

if hora >= 00 and hora < 12:
    print(f'Olá, bom dia! Eu sou o Bot Solution e estou aqui para te ajudar.')
elif hora >= 12 and hora < 18:
        print(f'Olá, boa tarde! Eu sou o Bot Solution e estou aqui para te ajudar.')
else:
    print('Olá, boa noite! Eu sou o Bot Solution e estou aqui para te ajudar.')

print(f'Primeiramente por gentileza me informe o seu nome: ') #input de nome do cliente
name = input()

print(f'É um prazer te conhecer, {name.capitalize()}') #name.capitalize() serve para deixar a primeira letra maiúscula

print(f'Estou aqui para te ajudar no que for necessário!!')

print(f'Problemas comuns:\n 1 - Problema #1 \n 2 - Problema #2\n 3 - Problema #3\n 4 - Problema #4\n 5 - Falar com uma pessoa fisica') #problemas mais comuns

while True:
    problem = input('Por gentileza digite apenas o número que representa o seu problema dentro dessas opções: ') #input do número do problema

    if (problem) == ('1'):
        print('Escreva a melhor forma que descreve o problema comum na empresa.')
        while True:
            option_1 = input(f'Você já tentou ... S para sim e N para não.').lower()
            if (option_1) == ('s'):
                print('Nesse caso um atendente entrará em contato com você.')
                break
            if (option_1) == ('n'):
                print('tente reiniciar.')
                break
            else:
                print('Não entendi a sua resposta')
        break

    if (problem) == ('2'):
        print(f'Escreva a melhor forma que descreve o problema comum na empresa.')
        while True:
            option_2 = input(f'Você já tentou ... S para sim e N para não.').lower()
            if (option_2) == ('s'):
                print('Nesse caso um atendente entrará em contato com você.')
                break
            if (option_2) == ('n'):
                print('tente reiniciar.')
                break
            else:
                print('Não entendi a sua resposta')
        break

    if (problem) == ('3'):
        print(f'Escreva a melhor forma que descreve o problema comum na empresa.')
        while True:
            option_3 = input(f'Você já tentou ... S para sim e N para não.').lower()
            if (option_3) == ('s'):
                print('Nesse caso um atendente entrará em contato com você.')
                break
            if (option_3) == ('n'):
                print('tente reiniciar.')
                break
            else:
                print('Não entendi a sua resposta')
        break

    if (problem) == ('4'):
        print(f'Escreva a melhor forma que descreve o problema comum na empresa.')
        while True:
            option_3 = input(f'Você já tentou ... S para sim e N para não.').lower()
            if (option_3) == ('s'):
                print('Nesse caso um atendente entrará em contato com você.')
                break
            if (option_3) == ('n'):
                print('tente reiniciar.')
                break
            else:
                print('Não entendi a sua resposta')
        break
    if (problem) == ('5'):
        print(f'Um atendente entrará em contato com você agora pelo proprio site.')
        break
    else:
        print(f'Infelizmente não consegui entender o que você digitou, poderia digitar novamente o número escolhido?')

print('Aguarde um momento, um de nossos atendentes está entrando no chamado para te auxiliar.') #encaminhamento para uma pessoa fisica