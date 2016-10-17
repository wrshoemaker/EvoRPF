from __future__ import division
import pandas as pd
import  matplotlib.pyplot as plt
import os, argparse, math, itertools
import numpy as np

mydir = os.path.expanduser('~/github/EvoRPF/')



def RPFhist():
    IN = pd.read_csv(mydir + 'data/clean/rpf_gene_copies_w_taxa_clean.txt', sep = ',')
    RPFs = IN.freq.values
    print RPFs.tolist().count(6)
    fig, ax = plt.subplots()
    ax.hist(RPFs, max(RPFs))
    ax.set_xlabel('RPF copy number', fontsize=20)
    ax.set_ylabel('Genomes', fontsize=20)
    fig.savefig(mydir + 'figs/test.png', \
        bbox_inches = "tight", pad_inches = 0.4, dpi = 600)
    plt.close()

RPFhist()
