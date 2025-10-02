def calcularSegundos(horas=0, minutos=0, segundos=0):
    totalSegundos = horas * 3600 + minutos * 60 + segundos
    return totalSegundos

def calcularHorasMinutosSegundos(totalSegundos):
    horas = totalSegundos // 3600
    minutos = (totalSegundos % 3600) // 60
    segundos = totalSegundos % 60
    return horas, minutos, segundos

