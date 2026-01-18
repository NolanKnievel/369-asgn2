import duckdb
import sys
from datetime import datetime
import time
from input import get_input


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



def main():
    inputs = get_input()
    analyze_r_place_data(inputs[0], inputs[1], 'r_place.parquet')

main()