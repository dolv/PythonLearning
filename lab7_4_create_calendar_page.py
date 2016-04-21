import datetime

def create_calendar_page(month=None,year=None):
    header = """--------------------
MO TU WE TH FR SA SU
--------------------
"""
    body = ''
    TODAY = datetime.date.today()
    if year is None: year = TODAY.year
    month = month or TODAY.month # the same logic as above in different notation
    if any(type(argument) not in [int, long] for argument in [month, year]) \
            or year > datetime.MAXYEAR \
            or month > 12:
        return False
    day = 1
    new_date = datetime.date(year, month, day)
    months_days = (datetime.date(new_date.year+(new_date.month+1)/12, new_date.month % 12+1, 1) - datetime.timedelta(days = 1)).day
    body += ' ' * 3 * new_date.weekday() + str(day).zfill(2)
    while day < months_days:
        day += 1
        new_date = datetime.date(year, month, day)
        body += ['\n',' '][new_date.weekday()>0]
        body += str(day).zfill(2)
    return header + body

print create_calendar_page(1)
print create_calendar_page()
print create_calendar_page(3)
print create_calendar_page(04, 1992)