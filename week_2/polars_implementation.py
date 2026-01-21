import polars
from datetime import datetime
import time
from input import get_input


def analyze_r_place_data(start_dt, end_dt, data_file):
    print(f"inputs: {start_dt}, {end_dt}, {data_file}")
    # start timing
    start_time = time.perf_counter_ns()

    # read parquet file
    df = polars.scan_parquet(data_file).filter(
        (polars.col("timestamp") >= start_dt) & 
        (polars.col("timestamp") < end_dt))

    # most placed color
    most_placed_color = (
        df
        .group_by("pixel_color")
        .agg(polars.len().alias("color_count"))
        .sort("color_count", descending=True)
        .limit(1)
        .collect()
    )
    
    # most placed pixel location
    most_placed_location = (
        df
        .group_by("coordinate")
        .agg(polars.len().alias("location_count"))
        .sort("location_count", descending=True)
        .limit(1)
        .collect()
    )
    
    print(f"Most Placed Color: {most_placed_color.to_dicts()}")
    print(f"Most Placed Location: {most_placed_location.to_dicts()}")
    
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    print(f"Elapsed Time: {elapsed_time} ns")
    print(f"elapsed time: {elapsed_time / 1000000} ms")
    print(f"elapsed time: {elapsed_time / 1000000000} s")

    return

def main():
    inputs = get_input()
    analyze_r_place_data(inputs[0], inputs[1], 'r_place.parquet')


main()