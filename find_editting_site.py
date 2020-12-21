import pandas as pd
import pickle
from intervaltree import Interval, IntervalTree

def find_intervals(row, r_tree):
    res = sorted(r_tree[row['chromosome']][row['position']])
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
    tbl = pd.read_csv("Human_AG_all_hg19.txt", sep='\t')
    f = open('intervals_to_transcript.pickle','rb')
    r_tree = pickle.load(f)
    tbl['Interval'] = tbl.apply(find_intervals, args=(r_tree,), axis=1)
    tbl = tbl.dropna()
    transcript_to_editing = get_key_vals(tbl['chromosome'], tbl['position'], tbl['Interval'])
    pickle.dump(transcript_to_editing, open( "transcript_to_editing.pickle", "wb" ) )
