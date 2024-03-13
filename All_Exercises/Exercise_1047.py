""" Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.

Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

Entrada
Quatro números inteiros representando a hora de início e fim do jogo.

Saída
Mostre a seguinte mensagem: O JOGO DUROU X HORA(S) E YYY MINUTO(S) ."""

# Ler a hora inicial, minuto inicial, hora final e minuto final do jogo
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Calcular a duração do jogo
hora_duracao = hora_final - hora_inicial
minuto_duracao = minuto_final - minuto_inicial

if minuto_duracao < 0:
    minuto_duracao += 60
    hora_duracao -= 1

if hora_duracao < 0:
    hora_duracao += 24

# Mostrar a duração do jogo com a mensagem correspondente
if hora_duracao == 0 and minuto_duracao == 0:
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hora_duracao, minuto_duracao))
                                                                                                                