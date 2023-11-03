
import csv
from datetime import datetime as dt

class Format_date():

    def __init__(self) -> None:
        self.date_time = []

    def split_datetime(self):
        # split datetime into date and time
        now = dt.now()
        str_dt = str(now)
        split = str_dt.split()
        return split
        
    def format_date(self):
        # format date
        split_dt = self.split_datetime()
        split_date = split_dt[0].split('-')
        date_str = f"{split_date[1]}/{split_date[2]}/{split_date[0]}"
        self.date_time.append(date_str)

    def format_time(self):
        # format time
        split_dt = self.split_datetime()
        split_time = split_dt[1].split(':')
        hour = split_time[0]
        int_hour = int(hour)
        if int_hour % 12 == 0:
            int_hour = 12
        else:
            int_hour = int_hour%12
        time_str = f"{int_hour}:{split_time[1]}"
        self.date_time.append(time_str)

    def return_dtformat(self):
        self.format_date()
        self.format_time()
        return self.date_time

def write_to_csv(data):
    filename = "points_db.csv"
    with open(filename, "a") as file:
        writer = csv.writer(file, delimiter=",", quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerow(data)
    return

def latest_total():
    filename = "points_db.csv"
    with open(filename, "r") as file:
        file_handler = list(csv.reader(file, delimiter=','))
    total = file_handler[-1][4]
    return total


def format_logging_points(btn_name: str, points: int, total: str):
    """Takes info from button,
        Takes info from datetime
        updates total
        inputs into write_to_csv() via dict"""
    format_dt = Format_date()
    str_points = str(points)
    date,time = format_dt.return_dtformat()
    new_row = [btn_name,str_points,time,date,total]
    write_to_csv(new_row)
    return
