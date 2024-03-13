# Declaration of variavles
n1, n2, n3, n4 = map(float, input().split())

# Media formula
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4)/10

# If Clause 
if media >= 7:
    print('Media: {:.1f}\nAluno aprovado.'.format(media))
elif media <= 6.9 and media >= 5:
    print('Media: {:.1f}\nAluno em exame.'.format(media))
    new = float(input())
    print("Nota do exame: {:.1f}".format(new))
    new_media = (media + new)/2
    if new_media > 5:
        print('Aluno aprovado.\nMedia final: {:.1f}'.format(new_media))
else:
    print('Media: {:.1f}\nAluno reprovado.'.format(media))