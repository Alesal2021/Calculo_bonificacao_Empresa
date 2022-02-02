#s1 = int(input('Digite se salario:'))
#s2 = int(input('Digite seu tempo de empresa:'))
#if s2 >= 5:
    #acr = (s1 * 20) / 100
    #res = s1 + acr
    #print('Seu tempo de empresa e {} anos, seu salrio sera = R${} '.format(s2,res))
#elif s2 <=4:
    #acr = (s1 * 10) / 100
    #res = s1 + acr
    #print('Seu tempo de empresa e {} anos, seu salario sera = R${} '.format(s2,res))
ano = int(input('Digite o ano de admissão na empresa: '))
ano_atual = int(input('Digite o ano que estamos: '))
salario = int(input('Digite seu salrio: '))
tempo = ano_atual - ano
if tempo >= 5:
    bonus = salario * 0.2
else:
    bonus = salario * 0.1
print('Seu ano de admissão foi {}'.format(ano))
print('Seu tempo de empresa e {}:'.format(ano_atual - ano))
print('Seu salario e {}'.format(salario))
print('Sua bonificão e {}'.format(bonus))
print('Seu salario com mais a bonificação sera {} '.format(salario + bonus))





