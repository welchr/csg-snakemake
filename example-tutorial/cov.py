#!/usr/bin/env python3
import pandas as pd
import sys, os, time

df = pd.read_table(sys.argv[1])

# For illustration purposes, let's create an output file immediately
# to see what happens if we cancel snakemake in the middle of the run
os.system(f"touch {sys.argv[2]}")

# Calculate covariance for genes on this chromosome
samples = [x for x in df.columns if x.startswith("S")]
cov = df.loc[:,samples].T.cov()
cov.columns = list(df.gene)
cov.index = list(df.gene)

cov.to_csv(sys.argv[2],sep="\t")
