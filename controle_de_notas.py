#Histórico Aluno

aluno = input('Nome do Aluno: ')
serie= input('Série do Aluno: ')
turma = input('Turma: ')
turno = input('Turno: ')
materia = input('Matéria: ')

n1 = float(input('Digite a primeira Nota: '))
n2 = float(input('Digite a segunda Nota: '))
n3 = float(input('Digite a terceira Nota: '))
n4 = float(input('Digite a quarta Nota: '))

total = int(n1+n2+n3+n4)

media = total / 4

print('A soma das notas do ano letivo = ',total)
print('A média final do aluno(a) - ',aluno, 'foi : ',media)

if media >= 7:
    print('Parabéns',aluno,'você foi aprovado(a)!')
else:
    print(aluno,'- Infelizmente você não atingiu a média, você foi reprovado(a)!')