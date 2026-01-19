import duckdb
import sys
from datetime import datetime
import time


def get_input():
    if len(sys.argv) < 5:
        print("Please provide start and end dates with hours.")
        return

    start_date = sys.argv[1]
    start_hour = sys.argv[2]
    end_date = sys.argv[3]
    end_hour = sys.argv[4]

    if not start_date or not end_date:
        print("Please provide both start and end dates.")
        return


    # cast arrs to ints
    start_year, start_month, start_day = map(int, start_date.split("-") )
    end_year, end_month, end_day = map(int, end_date.split("-"))
    start_hour = int(start_hour)
    end_hour = int(end_hour)

    start = datetime(start_year, start_month, start_day, start_hour)
    end = datetime(end_year, end_month, end_day, end_hour)
    
    # ensure end after start
    if end < start:
        print("End date must be after start date.")
        return


    print(f"Start Date: Year={start_year}, Month={start_month}, Day={start_day}, Hour={start_hour}")
    print(f"End Date: Year={end_year}, Month={end_month}, Day={end_day}, Hour={end_hour}")

    return (start, end)
