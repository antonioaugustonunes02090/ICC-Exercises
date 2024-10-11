import datetime
import dateutil.relativedelta as reldelta
date = datetime.datetime.strptime(input(),'%d/%m/%Y')
now = datetime.datetime(2024,4,4)
def get_time_from_birthday(today,birth):
    delta = reldelta.relativedelta(now,date)
    message = f'{delta.years} anos, {delta.months} meses e {delta.days+1} dias'
    return message
print(get_time_from_birthday(now,date))

