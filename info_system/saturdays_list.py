from datetime import date, timedelta

def past_saturdays(num):
    today = date.today()
    if today.weekday()==5:
        first_saturday = today
    elif today.weekday()<5:
        first_saturday = (today-timedelta(days=today.weekday()))-timedelta(days=2)
    else:
        first_saturday = today-timedelta(days=1)
    count = 0
    next_saturday = first_saturday
    while(count<num):
        yield next_saturday
        next_saturday -= timedelta(days=7)
        count = count + 1

