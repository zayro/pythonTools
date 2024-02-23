import datetime
import email.utils

# Obtenga la fecha y la hora actuales
now = datetime.datetime.now()
print(now)

# Formatee la fecha y la hora
formatted_date = email.utils.formatdate(timeval=now)

# Imprima la fecha y la hora formateadas
print(formatted_date)