import polars as pl
def main()->None:
    s=pl.Series("nums", [1, 2, 3, None, 5])
    print(f"The series is {s}")
    print(f"The name of the series is {s.name}")
    print(f"The length of the series is {s.len()}")
    print(f"The null counts is {s.null_count()}")
    print(f"The series empty bool is {s.is_empty()}")

if __name__ == "__main__":
    main()