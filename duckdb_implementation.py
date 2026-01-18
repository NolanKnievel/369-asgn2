import duckdb
import sys
from datetime import datetime
import time


# duckdb.sql("DESCRIBE SELECT * FROM r_place_canvas_history.parquet").show()



def analyze_r_place_data(start_dt, end_dt, data_file):

    print(f"inputs: {start_dt}, {end_dt}, {data_file}")
    # start timing
    start_time = time.perf_counter_ns()

    # find most placed color
    query_most_placed_color = f"""
        SELECT pixel_color, COUNT(*) AS color_count
        FROM read_parquet('{data_file}')
        WHERE timestamp >= ? AND timestamp < ?
        GROUP BY pixel_color
        ORDER BY color_count DESC
        LIMIT 1;
    """
    result_color = duckdb.sql(query_most_placed_color, params=(start_dt, end_dt)).fetchall()

    # find most placed pixel location
    query_most_placed_location = f"""
        SELECT coordinate, COUNT(*) AS location_count
        FROM read_parquet('{data_file}')
        WHERE timestamp >= ? AND timestamp < ?
        GROUP BY coordinate
        ORDER BY location_count DESC
        LIMIT 1;
    """
    result_location = duckdb.sql(query_most_placed_location, params=(start_dt, end_dt)).fetchall()

    print(f"Most Placed Color: {result_color}")
    print(f"Most Placed Location: {result_location}")

    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} ns")
    print(f"elapsed time: {elapsed_time / 1_000_000} ms")
    print(f"elapsed time: {elapsed_time / 1_000_000_000} s")

    return


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



def main():
    inputs = get_input()
    analyze_r_place_data(inputs[0], inputs[1], 'r_place.parquet')

main()