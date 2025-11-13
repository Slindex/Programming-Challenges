import datetime as dt


def isFriday(year: int, month: int) -> bool:
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12")

    date = dt.date(year, month, 13).isoweekday()

    if date == 5:
        return True
    else:
        return False

def main():

    try:
        year = int(input("Please enter the year"))
        month = int(input("Please enter the month"))
    except ValueError:
        print("You must enter numeric values")
        return

    try:
        print(isFriday(year, month))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()