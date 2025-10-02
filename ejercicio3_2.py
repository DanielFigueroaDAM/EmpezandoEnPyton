
import ejercicio3_1

segundos= input( "introduce los segundos que quieres convertir a horas, minutos y segundos: " )
segundos= int(segundos)

horas, minutos, segundos = ejercicio3_1.calcularHorasMinutosSegundos(segundos)


print(f"{horas} horas, {minutos} minutos y {segundos} segundos")

horas, minutos, segundos = input( "introduce las horas, minutos y segundos separados por comas: " ).split(",")
horas= int(horas)
minutos= int(minutos)
segundos= int(segundos)
totalSegundos = ejercicio3_1.calcularSegundos(horas, minutos, segundos)

print( f"{horas} horas, {minutos} minutos y {segundos} segundos son {totalSegundos} segundos" )