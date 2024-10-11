import datetime
import dateutil.relativedelta as reldelta
date = datetime.datetime.strptime(input(),'%d/%m/%Y')
now = datetime.datetime(2024,4,4)
def get_time_from_birthday(today,birth):
    delta = reldelta.relativedelta(now,date)
    if delta.months == 1:
        message = f'{delta.years} anos, {delta.months} mes e {delta.days+1} dias'
    else:
        message = f'{delta.years} anos, {delta.months} meses e {delta.days+1} dias'
    return message
print(get_time_from_birthday(now,date))

