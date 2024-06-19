# Task: Write a python program that gives you the day of the week in which is your
# anniversay after n years starting from the current year.

# n and your date of birth are read from the keyboard.

# Hint: being about the days of the week you have to use DATETIME module.
# datetime module python --> docs.python.org/library/datetime.ntm
# your date of birth will be inputed in this format: yyyy-mm-dd


# Solution:

from datetime import date


def get_weekday(n: str, birthday: str) -> str:
    WEEKDAY = {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday',
               4: 'Friday', 5: 'Saturday', 6: 'Sunday'}

    try:
        years = int(n)
    except ValueError as e:
        return f'This error occurred: -> {e}. The year must be a number.'

    try:
        birth_date = date.fromisoformat(birthday)
    except ValueError as e:
        return f'This error occurred: -> {e}. The birthday must be in YYYY-MM-DD format.'

    future_year = date.today().year + years
    future_birthday = date(future_year, birth_date.month, birth_date.day)

    return WEEKDAY[future_birthday.weekday()]


if __name__ == '__main__':
    n = input('number of years: ')
    birthday = input('your birthday: (YYY-MM-DD): ')
    day = get_weekday(n, birthday)
    print(day)

