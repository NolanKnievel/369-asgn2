## DuckDb
- pros:
    - SQL-based
    - Works the fastest
    - doesn't load data into memory - directly on parquet
- cons: 
    - Requires prior sql knowledge

## Polars
- pros:
    - More readable syntax (than sql in duckdb)
    - faster than pandas
    - more memory efficient than ppandas
    - reminds me of streams in Java
    - cool name
- cons: 
    - dataframe - less flexible than sql

## Pandas
- pros:
    - apparently works very well with other python libraries
    - acts more like a spreadsheet - can be more intuitive

- cons: 
    - Very slow
    - Uses lots of memory


## My Opinion
After using these three libraries, I found that I like DuckDb the best. Duckdb integrated very easily with my prior sql knowledge, and it ran the fastest by far. I found the dataframes harder to use since I was unfamiliar with their syntaxes and had to comb through their docs.