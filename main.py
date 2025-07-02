def monthCalc(month):
    
    choice = {
    'january': 5,
    'february': 1,
    'march': 1,
    'april': 4,
    'may': 6,
    'june': 2,
    'july': 4,
    'august': 0,
    'september': 3,
    'october': 5,
    'november': 1,
    'december': 3
    }
    
    return choice[month.lower()]


def centuryCalc(year):
    
    year = (int(year) // 100) % 4
    
    if year == 0:
        return 0
    elif year == 1:
        return 5
    elif year == 2:
        return 3
    elif year == 3:
        return 1


def yearCalc(year, month):
    
    leap = 0
    
    copy = (int(year) % 100)
    
    if (copy % 4 == 0) and (month.lower() in ("january", "february")):
        leap = 1
    
    copy = (copy + copy // 4 + 1) % 7
    return copy - leap


def dateCalc(value):
    value = value % 7
    if value == 0:
        return "Sunday"
    if value == 1:
        return "Monday"
    if value == 2:
        return "Tuesday"
    if value == 3:
        return "Wednesday"
    if value == 4:
        return "Thursday"
    if value == 5:
        return "Friday"
    if value == 6:
        return "Saturday"


def main():
    day = input("Enter Day Here: ")
    month = input("Enter Month Here: ")
    year = input("Enter Year Here: ")
    
    value = int(day) + yearCalc(year, month) + centuryCalc(year) + monthCalc(month)
    
    date = dateCalc(value)
    
    print(date)


main()
