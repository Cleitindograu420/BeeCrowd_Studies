# Datas iniciais
dia_inicio = int(input().split()[1])
hora_inicio, minuto_inicio , segundo_inicio = map(int, input().split(':')) 


# Datas finais
dia_fim = int(input().split()[1])
hora_fim, minuto_fim, segundo_fim = map(int, input().split(':'))

segundos_inicio = int(hora_inicio) * 3600 + int(minuto_inicio) * 60 + int(segundo_inicio) # Conversão de horas, minutos e segundos do INICIO
segundos_fim = int(hora_fim) * 3600 + int(minuto_fim) * 60 + int(segundo_fim) # Conversão de horas, minutos e segundos do FIM

segundos_duracao = segundos_fim - segundos_inicio

dias_duracao = segundos_duracao // 86400 # 86400 são a quantidade de segundos em um dia
if segundos_inicio > segundos_fim:
    dias_duracao = dia_fim - dia_inicio - 1
else:
    dias_duracao = dia_fim - dia_inicio   
segundos_duracao = segundos_duracao % 86400 # O  resto é os segundos que estão no tempo da duração do evento, para calcular hora, minutos e segundos

horas_duracao = segundos_duracao // 3600 #  3600 são os segundos em uma hora
segundos_duracao = segundos_duracao % 3600 #  O que sobrou para calcular os minutos restantes

minutos_duracao = segundos_duracao // 60
segundos_duracao = segundos_duracao % 60

print('{} dia(s)'.format(dias_duracao))
print('{} hora(s)'.format(horas_duracao))
print('{} minuto(s)'.format(minutos_duracao))
print('{} segundo(s)'.format(segundos_duracao))
