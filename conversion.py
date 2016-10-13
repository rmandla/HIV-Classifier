import sys
from datascience import *
from Bio import SeqIO
fasta = sys.argv[1]
csv = sys.argv[2]
def convert(x, y):
    handle = open(x, "rU")
    hiv1gag = Table(['id', 'seq'])
    for record in SeqIO.parse(handle, "fasta"):
        hiv1gag.append([record.id, str(record.seq)])
    handle.close()
    hiv1gag.to_df().to_csv(y, index = False)

convert(fasta, csv)
