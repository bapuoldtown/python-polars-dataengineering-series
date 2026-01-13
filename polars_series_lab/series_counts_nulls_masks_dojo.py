import polars as pl 
def main():
    device_id = pl.Series("device_id", ["r1", None, "r2", "r3", None, "r4", "r5", None])
    
    #count the none and calculate the nine percentage 
    print(f"The device id length is {device_id.len()}")
    print(f"The none count is {device_id.null_count()}")
    # percentage f failure
    print(f"The percentage count is {device_id.len()/device_id.null_count()}")
    
    print("is_null()      :", device_id.is_null().to_list())
    print("is_null()      :", device_id.is_not_null().to_list())
    
    # Extract positions of missing values (important in debugging)
    missing_idx = device_id.is_null().arg_true().to_list()
    present_idx = device_id.is_not_null().arg_true().to_list()
    print("missing indexes:", missing_idx)
    print("present indexes:", present_idx)
    print(f"The list is {device_id.to_list()}")
    
    user_id   = pl.Series("user_id",   ["u1", "u2", None, "u4", None, "u6", "u7"])
    country   = pl.Series("country",   ["IN", None, None, "US", "IN", None, "DE"])
    purchase  = pl.Series("purchase",  [100, None, 50, None, None, 200, 150])

    print("user_id  :", user_id.to_list())
    print("country  :", country.to_list())
    print("purchase :", purchase.to_list())
    
    # Events where BOTH user_id and country are missing
    both_missing = user_id.is_null() & country.is_null()
    # Now use count function to calculate nit nukk values bruv
    print(f"The country with non null is {country.count()}")

if __name__ == "__main__":
    main()