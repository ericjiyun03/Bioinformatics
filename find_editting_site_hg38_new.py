import pandas as pd
import pickle
from intervaltree import Interval, IntervalTree
ref = ["chr"+str(item) for item in range(1, 23)] + ['chrX', 'chrY']

def clean_chromosomes(column):
    if column in ref:
        return column
    else:
        return None

def find_intervals(row, r_tree):
    res = sorted(r_tree[row['Region']][row['Position']])
    if len(res) > 0:
        return res
    else:
        return None

def get_key_vals(chromosome, position, Interval):
    trans_to_editing = {}
    for chrm, pos, ivals in zip(chromosome, position, Interval):
        for ival in ivals:
            if ival.data in trans_to_editing:
                trans_to_editing[ival.data].append((chrm, pos))
            else:
                trans_to_editing[ival.data] = [(chrm, pos)]
    return trans_to_editing


if __name__ == "__main__":
    tbl = pd.read_csv("TABLE1_hg38.txt", sep='\t')
    tbl["Region"] = tbl["Region"].apply(clean_chromosomes)
    print(len(tbl))
    tbl = tbl.dropna(subset=["Region"])
    print(len(tbl))
    f = open('intervals_to_transcript.pickle','rb')
    r_tree = pickle.load(f)
    print(len(r_tree['chr11']))
    print(r_tree['chr11'][134856641])
    tbl['Interval'] = tbl.apply(find_intervals, args=(r_tree,), axis=1)
    #tbl['Interval'] = tbl.apply(find_intervals, r_tree=r_tree, axis=1)
    tbl = tbl.dropna()
    print(tbl[0:3])
    #tbl.to_csv("transcript_site_gene.dat", sep='\t')
    transcript_to_editing = get_key_vals(tbl['Region'], tbl['Position'], tbl['Interval'])
    pickle.dump(transcript_to_editing, open( "transcript_to_editing_hg38_new.pickle", "wb" ) )
