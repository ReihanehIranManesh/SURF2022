import pandas as pd
import pickle

ALL_GOOGLE_TAGS = []
ALL_MEAD_TAGS = {}

# process all Google tags
with open("class-descriptions.csv", "r") as csv_file:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        google_tag = row[1]
        ALL_GOOGLE_TAGS.append(google_tag)

# find the intersection between Google and MIMSY
with open("MIMSYApprovedTags.csv", "r") as csv_file:
    df = pd.read_csv(csv_file)
    for index, row in df.iterrows():
        mead_tag = row[0].lower()
        singular_tag = ""
        if mead_tag[-3:] == "ies":
            singular_tag = mead_tag[:-3]
        elif mead_tag[-2:] == "es":
            singular_tag = mead_tag[:-2]
        elif mead_tag[-1:] == "s":
            singular_tag = mead_tag[:-1]

        for TAG in ALL_GOOGLE_TAGS:
            TMPTAG = TAG.lower()
            if mead_tag in TMPTAG or (singular_tag and singular_tag in TMPTAG):
                if not ALL_MEAD_TAGS.get(mead_tag):
                    ALL_MEAD_TAGS.update({mead_tag: [TAG]})
                else:
                    ALL_MEAD_TAGS[mead_tag].append(TAG)

print(ALL_MEAD_TAGS)

with open('intersection_dictionary_v2.pkl', 'wb') as diction_file:
    pickle.dump(ALL_MEAD_TAGS, diction_file)
