def calculate_minutes(age_years):
    DAYS_IN_YEAR=365.25
    HOURS_IN_DAY=24
    MINUTES_IN_HOUR=60

    total_days=age_years*DAYS_IN_YEAR
    total_hours=total_days*HOURS_IN_DAY
    total_mins=total_hours*MINUTES_IN_HOUR

    return round(total_days),round(total_hours),round(total_mins)
while True:
    try:
        age=float(input('Enter your age in years '))
        days,hours,mins=calculate_minutes(age)

        print(f'\n You are approx: ')
        print(f'{days} days old and ')
        print(f'{hours} hours old.')

        again=input('Would you like to try again?(y/n)').strip().lower()

        if again!='y':
            print('Good bye! ')
            break
    except:
        print('Print enter valid age in numbers.')