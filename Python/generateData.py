from __future__ import division
import os
import pandas as pd

mydir = os.path.expanduser('~/github/EvoRPF/')

def cleanMetadata():
    IN = mydir + 'data/raw/rpf_gene_copies_w_taxa.txt'
    lines = []
    for line in open(IN):
        line =  line.strip().split('\t')
        lines.append([x.replace('"', '') for x in line])
    df = pd.DataFrame(lines[1:],columns=lines[0])
    df.to_csv(mydir + 'data/clean/rpf_gene_copies_w_taxa_clean.txt', index = False)

cleanMetadata()
