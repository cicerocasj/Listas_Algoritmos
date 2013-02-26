import time
date = input('Date (dd/mm/yyyy): ')
try:
    valid_date = time.strptime(date, '%d/%m/%Y')
    print('date valid')
except ValueError:
    print('Invalid date!')