def transformacao(segundos):
    h = segundos // 3600
    r = segundos % 3600
    m = r // 60
    s = r % 60

    print(f"{h} horas, {m} minutos e {s} segundos")

seg = int(input("Digite o número de segundos: "))
transformacao(seg)