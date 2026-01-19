import pandas
import time
from input import get_input

def analyze_r_place_data(start_dt, end_dt, data_file):
    print(f"inputs: {start_dt}, {end_dt}, {data_file}")
    
    # start timing
    start_time = time.perf_counter_ns()

    # Read parquet file with filtering
    df = pandas.read_parquet(
        data_file,
        filters=[
            ('timestamp', '>=', start_dt),
            ('timestamp', '<', end_dt)
        ]
    )
    
    # most placed color
    most_placed_color = (
        df['pixel_color']
        .value_counts()
        .head(1)
    )
    
    # most placed pixel location
    most_placed_location = (
        df['coordinate']
        .value_counts()
        .head(1)
    )
    
    print(f"Most Placed Color: {most_placed_color.to_dict()}")
    print(f"Most Placed Location: {most_placed_location.to_dict()}")
    
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