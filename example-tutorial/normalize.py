#!/usr/bin/env python3
import pandas as pd
import sys

# Read in data
df = pd.read_table(sys.argv[1],sep="\t")
samples = [x for x in df.columns if x.startswith("S")]

# Normalize by column totals and gene length
# Not quite right but good enough for example
colsums = df.loc[:,samples].apply(sum,axis=0)
lengths = df.length / int(1E6)
df.loc[:,samples] = df.loc[:,samples].divide(lengths,axis=0).divide(colsums,axis=1)

# Write out normalized data
df.to_csv(sys.argv[2],sep="\t",index=False,float_format="%0.2f")
