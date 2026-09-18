from datetime import datetime
from datetime import date


def main():
    day = datetime.now().weekday()
    print(day)
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print(days[day])

    if day <= 4:
        print("Its a weekday")
        remaining = 5 - day
        print(remaining, "days until the weekend")
    elif day == 4:
        print("Its Friday!")
        print(remaining, "Just a day left until the weekend")
    else:
        print("Its the weekend!")

    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    print("These are the summer months:")
    print(months[5])
    print(months[6])
    print(months[7])

    month= date.today()
    print(month.month)

    seasons = ["Winter", "Spring", "Summer", "Autumn"]

    if month <= 2 or month == 12:
        season = 0
    elif month <= 5:
        season = 1
    elif month <= 8:
        season = 2
    else:
        season = 3

    print("It is", seasons[season])
if __name__ == "__main__":
    main()
