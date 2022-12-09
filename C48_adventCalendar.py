# EL CALENDARIO DE ADEVIENTO 2022
# Fecha publicación enunciado: 28/11/22
# Fecha publicación resolución: 05/12/22
# Dificultad: FÁCIL
# 
# Enunciado: Crea una función que reciba un objeto de tipo "Date" y retorne lo siguiente:
# - Si la fecha coincide con el calendario de aDEViento 2022: Retornará el regalo de ese día (a tu elección) y cuánto queda para que
# finalice el sorteo de ese día.
# - Si la fecha es anterior: Cuánto queda para que comience el calendario.
# - Si la fecha es posterior: Cuánto tiempo ha pasado desde que ha finalizado.
# Notas:
# - Tenemos en cuenta que cada día del calendario comienza a medianoche 00:00:00 y finaliza a las 23:59:59.
# - Debemos trabajar con fechas que tengan año, mes, día, horas, minutos y segundos.
# - 🎁 Cada persona que aporte su solución entrará en un nuevo sorteo del calendario de aDEViento hasta el día de su corrección
# (sorteo exclusivo para quien entregue su solución).
# 
# Creador de los retos semanales: https://github.com/mouredev
# Repositorio original de Mouredev: https://github.com/mouredev/Weekly-Challenge-2022-Kotlin

from datetime import datetime

def adventCalendar(date: datetime):
    START_DATE = datetime(2022, 12, 1, 0, 0, 0)
    END_DATE = datetime(2022, 12, 24, 23, 59, 59)

    if date >= START_DATE and date <= END_DATE: return "🎁"

    if date < START_DATE:
        return f"Aún faltan: {difTime(START_DATE, date)}"
    elif date > END_DATE:
        return f"Han pasado: {difTime(date, END_DATE)}"

def difTime(dateStart, dateEnd):
    # diferencia entre fechas
    dateDif = dateStart - dateEnd
    # calculamos los años, días, horas, minutos y segundos
    days = dateDif.days if dateDif.days < 365 else dateDif.days % 365
    years = dateDif.days // 365
    seconds = dateDif.seconds
    minutes = dateDif.seconds // 60
    hours = dateDif.seconds // 3600
    return f"{years} años, {days} días y {pad(hours)}:{pad(minutes)}:{pad(seconds)}"

# para que quede mejor el formato de la hora
def pad(t):
    return str(t) if t > 9 else "0" + str(t)

print(adventCalendar(datetime(2022, 12, 1))) # 🎁
print(adventCalendar(datetime(2022, 12, 24, 23, 59, 59))) # 🎁
print(adventCalendar(datetime.today())) # Aún faltan: 0 años, 1 dias y 11:50:07
print(adventCalendar(datetime(2023, 1, 24, 23, 59, 59))) # Han pasado: 0 años, 31 días y 00:00:00