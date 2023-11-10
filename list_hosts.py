#!/usr/bin/env python3

import polars as pl

df = pl.read_csv("hosts.tsv", separator="\t")

# Filter rows based on the "Connection Type" field.
wired_df = df.filter(pl.col("Connection Type") == "Wired")
fiveg_df = df.filter(pl.col("Connection Type") == "5G")
twog_df = df.filter(pl.col("Connection Type") == "2.4G")

# Display the filtered DataFrame.
with pl.Config() as cfg:
    # Show all rows.
    # https://pola-rs.github.io/polars/py-polars/html/reference/config.html
    cfg.set_tbl_rows(-1)
    print(wired_df)
    print(fiveg_df)
    print(twog_df)
