#!/usr/bin/env python3

import polars as pl

df = pl.read_csv("hosts.tsv", separator="\t")

# Filter rows based on the "Connection Type" field.
wired_df = df.filter(pl.col("Connection Type") == "Wired")
fiveg_df = df.filter(pl.col("Connection Type") == "5G")
twog_df = df.filter(pl.col("Connection Type") == "2.4G")

# Display the filtered DataFrame.
print(wired_df)
print(fiveg_df)
print(twog_df)
