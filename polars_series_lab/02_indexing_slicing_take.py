import polars as pl 
def main():
    s = pl.Series("nums", [10, 20, 30, 40, 50, 60])
    print("s[0]:", s[0])
    print("s[0]:", s[-1])
    print(f"The slice from {s[2:4]}")

if __name__ == "__main__":
    main()