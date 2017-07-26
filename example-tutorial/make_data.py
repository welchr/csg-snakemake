#!/usr/bin/env python3
import pandas as pd
import numpy as np
import string, random, sys

rows = int(sys.argv[1])

def rand_gene():
  code = "".join((random.choice(string.ascii_uppercase) for _ in range(3)))
  num = np.random.randint(1,10)
  return code + str(num)

df = pd.DataFrame(np.random.uniform(0,150,size=(rows,5)).round().astype(int))
df.columns = [f"S{i}" for i in range(1,df.shape[1]+1)]
df.insert(0,"gene",[rand_gene() for _ in range(len(df))])
df.insert(1,"chrom",np.random.randint(1,5,size=rows))
df.insert(2,"length",np.random.randint(1000,99999,size=rows))

df.to_csv("gene_data.tab",sep="\t",index=False,float_format="%0.3f")
