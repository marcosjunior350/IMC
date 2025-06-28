print('\nCÁLCULO DO IMC - VERIFIQUE SE VOCÊ ESTÁ NO PESO IDEAL\n')

peso = float(input('Qual é o seu peso? (kg)\n'))
altura = float(input('Qual é a sua altura? (m)\n'))
imc = peso / (altura ** 2)

print('\nSeu IMC é de {:.2f}'.format(imc) + '.')

if imc < 18.5:
    print('Você está abaixo do peso. Recomendamos que procure um médico para avaliação criteriosa do resultado. '
'Pode indicar um estado de consumo do organismo, com poucas reservas e riscos associados.\n')
    
elif imc >= 18.5 and imc < 25:
    print('Você está no peso adequado. Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros da '
    'composição corporal, para compreender se estão dentro do recomendado. Algumas pessoas apresentam IMC dentro da '
    'normalidade, mas têm circunferência abdominal maior que a recomendada e/ou quantidade de massa gorda acima do ideal.\n')

elif imc >= 25 and imc < 30:
    print('Você está em sobrepeso. O sobrepeso está associado ao risco de doenças como diabetes e hipertensão. '
    'Então, atenção! Consulte um médico e reveja hábitos para reverter o quadro. ' 
    'Também é importante avaliar outros parâmetros, como a circunferência abdominal.\n')

elif imc >=30 and imc < 35:
    print('Você está com obesidade grau I. É importante buscar orientação médica e nutricional para entender melhor o seu caso, '
    'mesmo que os exames (colesterol e glicemia, por exemplo) estejam normais.\n')

elif imc >= 35 and imc < 40:
    print('Você está com obesidade grau II. Indica um quadro de obesidade mais evoluído em relação à classificação anterior e, '
          'mesmo com exames laboratoriais dentro da normalidade, não se deve atrasar a busca por orientação médica e nutricional.\n')

elif imc >=40:
    print('Você está com obesidade grau III. Nesse ponto, a chance de já estarmos diante de outras doenças associadas é mais elevada. '
          'É fundamental buscar orientação médica.\n')