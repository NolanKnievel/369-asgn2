import sys
import csv
from datetime import datetime
import time

def main():
    # start timing
    start_time = time.perf_counter_ns()

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


    # track counts in dictionaries
    color_counts = {}
    coordinate_counts = {}

    with open('2022_place_canvas_history.csv', 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            # Row 994: {'timestamp': '2022-04-04 01:42:45.074 UTC', 'user_id': 'JgBK0cLS7GStMGWGYWCjZpeVfdntdmZzcT3Ag8iubPuHNGkF5JKHhyhUaV1V5/2UlGHRKLeYMEhs9+wCNpYd/Q==', 'pixel_color': '#94B3FF', 'coordinate': '1706,572'}

            # get timestamp components
            timestamp_str = row['timestamp'].split('.')[0]
            date_str, time_str = timestamp_str.split(' ')[:2]
            year, month, day = map(int, date_str.split('-'))
            hour, minute, second = map(int, time_str.split(':'))

            timestamp = datetime(year, month, day, hour)

            # check if within date range
            if start <= timestamp < end:
                color = row['pixel_color']
                coordinate = row['coordinate']

                # update counts
                color_counts[color] = color_counts.get(color, 0) + 1
                coordinate_counts[coordinate] = coordinate_counts.get(coordinate, 0) + 1

            # print progress
            if i % 1000000 == 0:
                print(f"Processed {i} rows...")
                print(f"Current color counts: {len(color_counts)}")
                print(f"Current coordinate counts: {len(coordinate_counts)}")


    # print date range
    print(f"Date range: {start} to {end}")
    # get most common color and coordinate
    if color_counts:
        most_common_color = max(color_counts, key=color_counts.get)
        print(f"Most common color: {most_common_color} (Count: {color_counts[most_common_color]})")

    if coordinate_counts:
        most_common_coordinate = max(coordinate_counts, key=coordinate_counts.get)
        print(f"Most common coordinate: {most_common_coordinate} (Count: {coordinate_counts[most_common_coordinate]})")

    # stop timing
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time

    print(f"Elapsed ns: {elapsed_time}")
    print(f"Elapsed ms: {elapsed_time / 1_000_000}")
    print(f"Elapsed s: {elapsed_time / 1_000_000_000}")
    print(f"Elapsed min: {elapsed_time / 60_000_000_000}")

    rows_in_range = sum(color_counts.values())  # Total of all counts

    print(f"\nRows in date range: {rows_in_range}")
    print(f"Unique colors found: {len(color_counts)}")
    print(f"Unique coordinates found: {len(coordinate_counts)}")

    # Show top 5 colors
    print("\nTop 5 colors:")
    sorted_colors = sorted(color_counts.items(), key=lambda x: x[1], reverse=True)
    for color, count in sorted_colors[:5]:
        print(f"  {color}: {count:,}")

    # Show top 5 coordinates  
    print("\nTop 5 coordinates:")
    sorted_coords = sorted(coordinate_counts.items(), key=lambda x: x[1], reverse=True)
    for coord, count in sorted_coords[:5]:
        print(f"  {coord}: {count:,}")


if __name__ == "__main__":
    main()
