
def is_leap_year(year):
    if (year % 100 == 0) & (year % 400 != 0):
        return False
    elif year % 4 == 0:
        return True
    return False
