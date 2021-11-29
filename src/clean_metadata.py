import pandas as pd

"""
Script for cleaning the HMP2 metadata for easier parsing and
filtering of samples and knowing thier disease condition
The subject_ids.txt file is generated using the following command

$ head -1 ./Data/taxonomic_profiles.tsv |\
        tr '\t' '\n' |\
        tail -n+2 |\
        head -n-1 >| ./Data/subject_ids.txt
"""

# read data into pandas
df = pd.read_csv('./Data/hmp2_metadata.csv')
# self explanatory
df = df[df['Did the subject withdraw from the study?'] == 'No']
df = df[df['Was subject terminated by investigator?'] == 'No']
# filter any columns with 'recieved' in title (useless)
to_keep = [x for x in df.columns if 'received' not in x]
df = df[to_keep]
# filter columns with any null entries
df = df[df.columns[df.isnull().mean() < 0.10]]
# Only keep subjects we have abundance data for
subjects = [x.strip('\n') for x in open('./Data/subject_ids.txt').readlines()]
df = df[df['External ID'].isin(subjects)]
# drop all columns with no diversity
nunique = df.nunique()
cols_to_drop = nunique[nunique == 1].index
df.drop(cols_to_drop, axis=1)
# write to csv
vcs = {col: df[col].value_counts() for col in df.columns}
print([x for x, v in vcs.items() if len(v) > 1])
# print(df['diagnosis'].value_counts())
df.to_csv('./Data/filtered_hmp2_metadata.tsv', sep='\t', index=False)
