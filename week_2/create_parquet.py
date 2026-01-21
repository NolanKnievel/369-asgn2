import duckdb

duckdb.sql("PRAGMA enable_progress_bar;")

duckdb.sql("""
    COPY (SELECT 
        CAST(timestamp AS TIMESTAMP) as timestamp,
        coordinate,
        pixel_color,
        user_id

 FROM read_csv_auto('../../asgn1/2022_place_canvas_history.csv'))
    TO 'r_place2.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
""")

