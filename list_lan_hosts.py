#!/usr/bin/env python3

import polars as pl

df = pl.read_csv("lan-hosts.tsv", separator="\t")

# Filter rows based on the "Connection" field.
ethernet_df = df.filter(pl.col("Connection") == "Ethernet")
wifi_df = df.filter(pl.col("Connection").str.contains("Wi-Fi"))
# Filter rows based on the "Status" field.
status_df = df.filter(pl.col("Status") == "on")

# Display the filtered DataFrame.
print(ethernet_df)
print(wifi_df)
print(status_df)
