from datetime import datetime

begin_date_time = datetime(2021, 6, 14, 8, 0)


def book_vaccine():
    now = datetime.now()
    if now >= begin_date_time:
        return "開始預約"
    else:
        return "2021-06-14 08：00 才能預約"


if __name__ == "__main__":
    print(book_vaccine())
