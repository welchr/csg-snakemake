#!/usr/bin/env python3
from argparse import ArgumentParser
import pandas as pd

if __name__ == "__main__":
  argparser = ArgumentParser()
  argparser.add_argument("--infile",type=str,required=True)
  argparser.add_argument("--chrom",type=int,required=True)
  argparser.add_argument("--outfile",type=str,required=True)
  args = argparser.parse_args()

  df = pd.read_table(args.infile,sep="\t")
  subset = df[df.chrom == args.chrom]
  subset.to_csv(args.outfile,sep="\t",index=False)

